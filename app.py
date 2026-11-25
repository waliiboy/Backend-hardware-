from flask import *
import pymysql
# import helper module
from helper import upload_photo 

# initialize the app 
app=Flask(__name__)

                                         # register function 

# define the endpoint 
@app.route("/register", methods=["POST"])
# define signup function
def register():

    # 3.Get user inputs from the form
    username=request.form["username"]
    password=request.form["password"]
    email=request.form["email"]
    phone=request.form["phone"]
    role=request.form["role"]

    # 4.establish connection to database
    connection=pymysql.connect(host="mysql-waliiboy.alwaysdata.net", password="modcom2026", user="waliiboy",database="waliiboy_hardware")

    # 5.define your cursor
    cursor=connection.cursor()

    # 6.define sql to insert users
    sql="insert into users(username,password,email,phone,role) values(%s, %s, %s, %s, %s)"

    # 7.define your data 
    # NB:its coming from step 3
    data=(username,password,email,phone,role)

    # 8.execute/run query
    cursor.execute(sql, data)

    # 9.commit/save change
    connection.commit()

    # 10.give response to the user
    return jsonify({"message":"account created successfully"})

                                        # login function   


#1.define the endpoint/route
@app.route("/login", methods=["POST"])

#2.define signin function
def login():

    # 3.get user inputs from the form
    email=request.form["email"]
    password=request.form["password"]

    # 4.establish connection to database
    connection=pymysql.connect(user="waliiboy",host="mysql-waliiboy.alwaysdata.net",password="modcom2026",database="waliiboy_hardware")

    #5.define your cursor 
    cursor=connection.cursor(pymysql.cursors.DictCursor)

    # 6.sql to select 
    sql ="select *from users where email=%s and password=%s"

    # 7.define your data 
    # NB:comesfro step 3
    data= (email,password)

    # 8.execute/run query
    cursor.execute(sql,data)
    if cursor.rowcount==1:
        # fetch that user
        loginuser=cursor.fetchone()
        return jsonify ({"message":"login successful","user":loginuser})
    else:
        return jsonify({"message":"login failed"})


#1.define the endpoint
@app.route("/addproduct",methods=["POST"])

# 2.define addproduct function
def addproduct():
    # 3.get product inputs from the form 
    product_name=request.form["product_name"]
    category=request.form["category"]
    brand=request.form["brand"]
    description=request.form["description"]
    price=request.form["price"]

    product_photo=request.files["product_photo"]

    # 4.establish connection to database
    connection=pymysql.connect(host="mysql-waliiboy.alwaysdata.net",user="waliiboy",password="modcom2026",database="waliiboy_hardware")

    # 5.define your cursor
    cursor=connection.cursor()

    # 6.insert products 
    sql="insert into hardware_products(product_name,category,brand,description,price,product_photo) values(%s,%s,%s,%s,%s,%s)"

    # 7.define your data from step3
    data=(product_name,category,brand,description,price,upload_photo(product_photo))

    # 8.execute
    cursor.execute(sql,data)

    # 9.commit
    connection.commit()

    # 10.response to the user
    return jsonify({"message":"products added successfully"})



# 1.define the endpoint
@app.route("/getproducts")
# 2.define getproduct function
def getproducts():

    # 3.connection to database
    connection=pymysql.connect(user="waliiboy",host="mysql-waliiboy.alwaysdata.net",password="modcom2026",database="waliiboy_hardware")

    # 4.define your cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)

    # 5.define sql to select products
    sql="select * from hardware_products"

    # 6.execute/run query
    cursor.execute(sql)

    # 7.fetch all products
    allproducts=cursor.fetchall()

    # 8.return all products to the user 
    return jsonify (allproducts)

# app.run(debug=True)












































