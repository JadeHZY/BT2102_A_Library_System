import pymysql

def connection():
    con = pymysql.connect(host='localhost',user='root',password='Jadehzy666',db='ALS')
    return con
