import time
import pymysql

#预定用餐时间范围：时间戳 开始时间戳(time)-结束时间戳(time)
def gettimes():
    time_format = "%Y-%m-%d %H:%M:%S"
    day = time.strftime('%Y-%m-%d')
    list = []
    #早市时间戳
    mon_market1 = day + " 8:00:00"
    mon_array1 = time.strptime(mon_market1,time_format)
    mon_stamp1 = int(time.mktime(mon_array1))
    list.append(mon_stamp1)
    mon_market2 = day + " 10:00:00"
    mon_array2 = time.strptime(mon_market2, time_format)
    mon_stamp2 = int(time.mktime(mon_array2))
    list.append(mon_stamp2)
    #午市时间戳
    after_market1 = day + " 11:00:00"
    after_array1 = time.strptime(after_market1, time_format)
    after_stamp1 = int(time.mktime(after_array1))
    list.append(after_stamp1)
    after_market2 = day + " 15:00:00"
    after_array2 = time.strptime(after_market2, time_format)
    afer_stamp2 = int(time.mktime(after_array2))
    list.append(afer_stamp2)

    # 晚市时间戳
    even_market1 = day + " 18:00:00"
    even_array1 = time.strptime(even_market1, time_format)
    even_stamp1 = int(time.mktime(even_array1))
    list.append(even_stamp1)
    even_market2 = day + " 23:00:00"
    even_array2 = time.strptime(even_market2, time_format)
    even_stamp2 = int(time.mktime(even_array2))
    list.append(even_stamp2)
    return list
#预定时段
def getrdate():
    now = int(time.time())
    times = gettimes()
    if  now < times[2]:
        rdate = str(times[2]) + "-" + str(times[3])
    elif now > times[2] and now < times[4]:
        rdate = str(times[4]) + "-" + str(times[5])
    elif now > times[4]:
        rdate = str(times[0]+86400) + "-" + str(times[1]+86400)
    return rdate
#预定到店时间
def getddate():
    now = int(time.time())
    times = gettimes()
    if now < times[2]:
        ddate = times[2] + 5400
    elif now > times[2] and now < times[4]:
        ddate = times[4] + 5400
    elif now > times[4]:
        ddate = times[0]+86400
    return ddate

def connectMysql(sql,fetch="one"):
    conn = pymysql.connect(host="101.201.37.61", user="readuser", password="Naji2018", database="xt-member-two-LINE",
                           charset="utf8")
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        if "one" == fetch:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        return result
    except Exception as e:
        raise e
def getstatus(id):
    sql = "select status from xt_dc_reserve where id = {}".format(id)
    return str(connectMysql(sql)[0])
def getAction(rid):
    sql = "select action from xt_dc_reserve where id = {}".format(rid)
    return connectMysql(sql)[0]











