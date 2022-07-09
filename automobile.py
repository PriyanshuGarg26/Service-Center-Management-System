import tkinter 
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,simpledialog
import pymysql
from datetime import date
from tkinter import ttk
import smtplib
import random
import matplotlib.pyplot as plt

def code():
    a=str(random.randint(1000,9999))
    today = date.today()

    # dd/mm/YY
    d1 = today.strftime("%d%m%Y")
    
    return(d1+a)
def email():

    s=smtplib.SMTP('smtp.gmail.com',587)
    #Unique Code
    cur.execute("select complainid from Call_Assign where PCATID='%s'"%pcidi.get())
    codeid=cur.fetchone()
    cur.execute("select Email from customer where custid='%s'"%cstidi.get())
    custemail=cur.fetchone()
    cur.execute("select name from customer where custid='%s'"%cstidi.get())
    custname=cur.fetchone()
    cur.execute("select address from customer where custid='%s'"%cstidi.get())
    custaddress=cur.fetchone()

    s.starttls()
    s.login('xyz@gmail.com','Password')
    #message='Name-              '+str(custname)+'\n'+'Address-              '+str(custaddress)+'\n'+'Product Category ID-       '+pcidi.get()+'\n'+'\n'+'Engineer-ID-               '+eidi.get()+'\n'+'complainid-                  '+str(codeid)+'\n'+'charges-                  '+cgti.get()
    message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Invoice

<!DOCTYPE html>
<html>
<head>
    <title></title>
    <style type="text/css">
    th, td {
  padding: 15px;
    </style>
</head>
<body>
<table border="1" style="width:40vw;text-align:center;border:3px grooved brown;box-shadow:0 0 20px -2px #aaa;">
    <tr>
        <th> Name </th>
        <th>Address </th>
        <th>Product Category ID</th>
        <th>Engineer ID</th>
        <th>Complain ID</th>
        <th>Charges</th>
    </tr>
    <tr>
        <td>""" + str(custname) + """</td>
        <td>""" + str(custaddress) + """</td>
        <td>""" + str(pcidi.get()) + """</td>
        <td>""" + str(eidi.get()) + """</td>
        <td>""" + str(codeid) + """</td>
        <td>""" + str(cgti.get()) + """</td>
    </tr>
</table>
</body>
</html>
    """
    s.sendmail('xyz@gmail.com',custemail,message)
    print('Mail sent')
    messagebox.showinfo('E-mail','E-mail sent')

    s.quit()


db=pymysql.connect(host='localhost',user='root',password='root',db='SC')
cur=db.cursor()

t=tkinter.Tk()
# t.geometry('1200x1200')
t.title('Service Center Application')
t.config(bg='lightblue')
# t.attributes('-fullscreen',True)
width=t.winfo_screenwidth()
height=t.winfo_screenheight()
t.geometry("%dx%d"%(width,height))
#list of existing data
cur.execute('select PCATID from product_category')
expcid=list(cur.fetchall())

cur.execute('select PID from product')
expid=list(cur.fetchall())

cur.execute('select SERID from SERVICE_TYPE')
exsid=list(cur.fetchall())              #service id

cur.execute('select CUSTID from CUSTOMER')
excustid=list(cur.fetchall())

cur.execute('select ENGID from engineers')
exengid=list(cur.fetchall())

cur.execute('select STAFFID from call_center')
exstfid=list(cur.fetchall())


scn=Label(t,text='Service Center Admin Login Page',bg='blue',fg='White',height=2,width=60)
scn.place(x=0,y=0)
scn.config(font=('Helvetica bold',30))

c=Canvas(t,height=200,width=1300,bg='Aquamarine')
c.place(x=0,y=500)
img=ImageTk.PhotoImage(Image.open("automobile.png"))
c.create_image(180,100,image=img)
img1=ImageTk.PhotoImage(Image.open("automobile1.png"))
c.create_image(580,90,image=img1)
img2=ImageTk.PhotoImage(Image.open("automobile2.png"))
c.create_image(1040,80,image=img2)

ad=Label(t,text='Admin ID',bg='lightblue')
ad.place(x=370,y=220)
ad.config(font=('Helvetica bold',15))
adi=Entry(t,width=40)
adi.place(x=480,y=220)

pwd=Label(t,text='Password',bg='lightblue')
pwd.place(x=370,y=270)
pwd.config(font=('Helvetica bold',15))
passi=Entry(t,width=40,show='*')
passi.place(x=480,y=270)


def check():
    psc=passi.get()
    if psc=='root':
        
        messagebox.showinfo('Welcome','welcome')
        def choice():
            # p=Toplevel()
            # p.geometry('300x300')
            # p.config(bg='Aquamarine')
            ch=int(aa.get())
            #PRODUCT CATEGORY INFORMATION 
            if ch==0: 
                p=Toplevel()
                p.geometry("%dx%d"%(width,height))
                p.config(bg='lightblue')
                
                def enterdetails():
                    hd=Label(p,text='Enter the Details')
                    hd.place(x=100,y=100)
                    hd.config(font=('Helvetica bold',20))
                    
                
                    pcid=Label(p,text='Product Category ID')
                    pcid.place(x=100,y=150)
                    current_value4 = StringVar(value='Must be start with PC')
                    global pcidi
                    pcidi=Entry(p,width=40,textvariable=current_value4)
                    pcidi.place(x=250,y=150)
                    
                    cn=Label(p,text='Category Name')
                    cn.place(x=100,y=200)
                    cni=Entry(p,width=40)
                    cni.place(x=250,y=200)
                    
                    ty=Label(p,text='Type')
                    ty.place(x=100,y=250)
                    tyi=Entry(p,width=40)
                    tyi.place(x=250,y=250)
                    
                    des=Label(p,text='Description')
                    des.place(x=100,y=300)
                    desi=Entry(p,width=40)
                    desi.place(x=250,y=300)
                    
                    def close1():
                        messagebox.showinfo('Thanks','Thanks')
                        p.destroy()
                        
                    close=Button(p,text='Back to Main Menu',command=close1)
                    close.place(x=350,y=350)
                    
                    def clsap():
                        messagebox.showinfo('Thanks','Thanks')
                        t.destroy()
                        
                    close=Button(p,text='Close Application',bg='Red',command=clsap)
                    close.place(x=350,y=400)                    
                    
                    def clr1():
                        pcidi.delete(0,100)
                        cni.delete(0,100)
                        tyi.delete(0,100)
                        desi.delete(0,100)
                        
                    clr=Button(p,text='Clear',command=clr1)
                    clr.place(x=250,y=400)
                    
                    def savedata_productcategory():
                        en1=pcidi.get()
                        en2=cni.get()
                        en3=tyi.get()
                        en4=desi.get()  
                        try:
                            if en1.startswith('PC')!=True :
                                raise Exception
                            else:
                                s="insert into product_category values('%s','%s','%s','%s')"%(en1,en2,en3,en4)
                                try:
                                    cur.execute(s)
        
                                    db.commit()
                                    messagebox.showinfo('Saved','Data Saved') 
                                    expcid.append(en1)
                                    pcidi.delete(0,100)
                                    cni.delete(0,100)
                                    tyi.delete(0,100)
                                    desi.delete(0,100)
                                    p.destroy()
                            #e.delete(0,100)
                                except Exception as ex:
                                   
                                    messagebox.showinfo('Error',ex) 
                             
                        except Exception:
                            messagebox.showinfo('Error',"Product Category ID should starts with 'P'")
                       
                        
                        
                                    
                    submit=Button(p,text='Submit',command=savedata_productcategory)
                    submit.place(x=250,y=350)
                    
                    

                def deletedata_productcategory():
                    name=simpledialog.askstring("Input","Enter the Product Category-ID",parent=p)
                        
                    
                    s="delete from product_category where PCatId='%s'"%(name)
                    try:
                        cur.execute(s)
                        #Save
                        db.commit()
                        
                        messagebox.showinfo('Delete','Data Deleted')
                        p.destroy()
                        #expcid.remove(name)    
                        
                        
                    except Exception as ex:
                        messagebox.showinfo('Error',ex) 


                submit=Button(p,text='Enter Details',command=enterdetails)
                submit.place(x=150,y=50)

                dlt=Button(p,text='DELETE RECORD',command=deletedata_productcategory)
                dlt.place(x=350,y=50)


            #PRODUCT INFORMATION
            elif ch==1: 
                p=Toplevel()
                p.geometry("%dx%d"%(width,height))
                p.config(bg='lightblue')
                def enterdetails():
                
                    hd=Label(p,text='Enter the Product Details')
                    hd.place(x=100,y=100)
                    hd.config(font=('Helvetica bold',20))
                    
                    pid=Label(p,text='Product ID')
                    pid.place(x=100,y=150)
                    current_value5 = StringVar(value='Must be start with P')
                    global pidi
                    pidi=Entry(p,width=40,textvariable=current_value5)
                    pidi.place(x=250,y=150)
                    
                    pcid=Label(p,text='Product Category ID')
                    pcid.place(x=100,y=200)
                    '''
                    pcidi=Entry(p,width=40)
                    pcidi.place(x=250,y=200)
                    '''
                    n = tkinter.StringVar()
                    pcidi = ttk.Combobox(p, width = 27, textvariable = n)
                    pcidi['values']=expcid
                    pcidi.place(x=250,y=200)

                    pn=Label(p,text='Product Name')
                    pn.place(x=100,y=250)
                    pni=Entry(p,width=40)
                    pni.place(x=250,y=250)
                    
                    cst=Label(p,text='Cost')
                    cst.place(x=100,y=300)
                    current_value3 = StringVar(value=0)
                    csti=Entry(p,width=40, textvariable = current_value3)
                    csti.place(x=250,y=300)
                    
                    def close1():
                        messagebox.showinfo('Thanks','Thanks')
                        p.destroy()
                        
                    close=Button(p,text='Back to Main Menu',command=close1)
                    close.place(x=350,y=350)
                    
                    def clsap():
                        messagebox.showinfo('Thanks','Thanks')
                        t.destroy()
                        
                    close=Button(p,text='Close Application',bg='Red',command=clsap)
                    close.place(x=350,y=400)                    
                    
                    def clr1():
                        pidi.delete(0,100)
                        pcidi.delete(0,100)
                        pni.delete(0,100)
                        csti.delete(0,100)
                        
                    clr=Button(p,text='Clear',command=clr1)
                    clr.place(x=250,y=400)                    
                    
                    
                    
                    def savedata_product():
                        en1=pidi.get()
                        en2=pcidi.get()
                        en3=pni.get()
                        if csti.get().isalpha():
                            messagebox.showinfo('Error','Charges Must be in Digits')
                        else:
                            en4=int(csti.get())
                        #en4=int(csti.get())

                        try:
                            if en1.startswith('P')!=True or en2.startswith('PC')!=True :
                                raise Exception
                            elif en4<1000:
                                class MyException(Exception):
                                    def message(self):
                                        messagebox.showinfo('Error','Minimum Price Should be Rs.1000')

                                try:
                                    
                                    raise MyException
                                except MyException as ex:
                                    ex.message()

                            else :
                                s="insert into product values('%s','%s','%s',%d)"%(en1,en2,en3,en4)
                                try:
                                    cur.execute(s)
        #Save
                                    db.commit()
                                    messagebox.showinfo('Saved','Data Saved')
                                    expid.append(en1)     
                                    pidi.delete(0,100)
                                    pcidi.delete(0,100)
                                    pni.delete(0,100)
                                    csti.delete(0,100)
                                    p.destroy()
                                    
                                    
                                    
                                except Exception as ex:
                                    messagebox.showinfo('Error',ex)


                        except Exception:
                            messagebox.showinfo('Error',"Product Category ID and Product ID should starts with 'PC' and 'P'")
    
                        
                    submit=Button(p,text='Submit',command=savedata_product)
                    submit.place(x=250,y=350)


                def deletedata_product():
                    name=simpledialog.askstring("Input","Enter the Product-ID",parent=p)
                            
                    
                    s="delete from product where PId='%s'"%(name)
                    try:
                        cur.execute(s)
                        #Save
                        db.commit()
                        messagebox.showinfo('Delete','Data Deleted')     
                        
                        #expid.remove(name)
                        
                    except Exception as ex:
                        
                        messagebox.showinfo('Error',ex)
                
                submit=Button(p,text='Enter Details',command=enterdetails)
                submit.place(x=150,y=50)

                dlt=Button(p,text='DELETE RECORD',command=deletedata_product)
                dlt.place(x=350,y=50)


            #SERVICE TYPES TABLE
            elif ch==2: 
                p=Toplevel()
                p.geometry("%dx%d"%(width,height))
                p.config(bg='lightblue')
                def enterdetails():
                
                    hd=Label(p,text='Enter the Service Details')
                    hd.place(x=100,y=100)
                    hd.config(font=('Helvetica bold',20))
                
                    sid=Label(p,text='Service ID')
                    sid.place(x=100,y=150)
                    global sidi
                    sidi=Entry(p,width=40)
                    sidi.place(x=250,y=150)
    
                    pid=Label(p,text=' Product ID')
                    pid.place(x=100,y=200)
                    #pidi=Entry(p,width=40)
                    n = tkinter.StringVar()
                    pidi = ttk.Combobox(p, width = 27, textvariable = n)
                    pidi['values']=expid
                    pidi.place(x=250,y=200)
                    
                    pcid=Label(p,text=' Product Category ID')
                    pcid.place(x=100,y=250)
                    #pcidi=Entry(p,width=40)
                    n = tkinter.StringVar()
                    pcidi = ttk.Combobox(p, width = 27, textvariable = n)
                    pcidi['values']=expcid
                    pcidi.place(x=250,y=250)
                    
                    sn=Label(p,text='Service Type Name')
                    sn.place(x=100,y=300)
                    sni=Entry(p,width=40)
                    sni.place(x=250,y=300)
                    
                    cgt=Label(p,text='Charges')
                    cgt.place(x=100,y=350)
                    current_value2 = StringVar(value=0)
                    cgti=Entry(p,width=40,textvariable =current_value2)
                    cgti.place(x=250,y=350)
                    
                    def close1():
                        messagebox.showinfo('Thanks','Thanks')
                        p.destroy()
                        
                    close=Button(p,text='Back to Main Menu',command=close1)
                    close.place(x=350,y=400)
                    
                    def clsap():
                        messagebox.showinfo('Thanks','Thanks')
                        t.destroy()
                        
                    close=Button(p,text='Close Application',bg='Red',command=clsap)
                    close.place(x=350,y=450)                    
                    
                    def clr1():
                        sidi.delete(0,100)
                        pidi.delete(0,100)
                        pcidi.delete(0,100)
                        sni.delete(0,100)
                        cgti.delete(0,100)
                        
                    clr=Button(p,text='Clear',command=clr1)
                    clr.place(x=250,y=450)                    
                    
                    
                    
                
                    def savedata_service():
                        en1=sidi.get()
                        en2=pidi.get()
                        en3=pcidi.get()
                        en4=sni.get() 
                        if cgti.get().isalpha():
                            messagebox.showinfo('Error','Charges Must be in Digits')
                        else:
                            en5=int(cgti.get())

                        try:
                            if en1.startswith('S')!=True or en2.startswith('P')!=True or en3.startswith('PC')!=True:
                                raise Exception
                            elif en5<100 :
                                class MyException(Exception):
                                    def message(self):
                                        messagebox.showinfo('Error','Minimum Charges Should be Rs.100')

                                try:
                                    
                                    raise MyException
                                except MyException as ex:
                                    ex.message()

                            else :
                                s="insert into service_type values('%s','%s','%s','%s',%d)"%(en1,en2,en3,en4,en5)
                                try:
                                    cur.execute(s)
        #Save
                                    db.commit()
                                    exsid.append(en1)
                                    messagebox.showinfo('Saved','Data Saved') 
                                    sidi.delete(0,100)
                                    pidi.delete(0,100)
                                    pcidi.delete(0,100)
                                    sni.delete(0,100)
                                    cgti.delete(0,100)
                                    p.destroy()
                                except Exception as ex:
                                    messagebox.showinfo('Error',ex)
                        except Exception:
                            messagebox.showinfo('Error',"Product Category ID and Product ID should starts with 'PC' and 'P'")
                            messagebox.showinfo('Error',"Service ID should starts with 'S'")                        

                    submit=Button(p,text='Submit',command=savedata_service)
                    submit.place(x=250,y=400)


                def deletedata_service():
                    name=simpledialog.askstring("Input","Enter the Service-ID",parent=p)
                    
                    s="delete from service_type where SERID='%s'"%(name)
                    try:
                        cur.execute(s)
                        #Save
                        db.commit()
                        exsid.remove(name)
                        messagebox.showinfo('Delete','Data Deleted') 
                            
                        
                        
                    except Exception as ex:
                        messagebox.showinfo('Error',ex)
                submit=Button(p,text='Enter Details',command=enterdetails)
                submit.place(x=150,y=50)

                dlt=Button(p,text='DELETE RECORD',command=deletedata_service)
                dlt.place(x=350,y=50)


            #ADD CUSTOMER TABLE
            elif ch==3: 
                p=Toplevel()
                p.geometry("%dx%d"%(width,height))
                p.config(bg='lightblue')
                def enterdetails():
                
                    hd=Label(p,text='Enter the Customer\'s Details')
                    hd.place(x=100,y=100)
                    hd.config(font=('Helvetica bold',20))
                    
                    cstid=Label(p,text='Customer Id')
                    cstid.place(x=100,y=150)
                    global cstidi
                    cstidi=Entry(p,width=40)
                    cstidi.place(x=250,y=150)
                    
                    cn=Label(p,text='Customer name')
                    cn.place(x=100,y=200)
                    global cni
                    cni=Entry(p,width=40)
                    cni.place(x=250,y=200)
                    
                    cad=Label(p,text='Address')
                    cad.place(x=100,y=250)
                    global cadi
                    cadi=Entry(p,width=40)
                    cadi.place(x=250,y=250)
                    
                    ceid=Label(p,text=' Customer E-Mail Id')
                    ceid.place(x=100,y=300)
                    global ceidi
                    ceidi=Entry(p,width=40)
                    ceidi.place(x=250,y=300)
                    
                    pcid=Label(p,text='Product Catgory Id')
                    pcid.place(x=100,y=350)
                    #pcidi=Entry(p,width=40)
                    n = tkinter.StringVar()
                    pcidi = ttk.Combobox(p, width = 27, textvariable = n)
                    pcidi['values']=expcid                    

                    pcidi.place(x=250,y=350)
                                    
                    def close1():
                        messagebox.showinfo('Thanks','Thanks')
                        p.destroy()
                        
                    close=Button(p,text='Back to Main Menu',command=close1)
                    close.place(x=350,y=400)
                    
                    def clsap():
                        messagebox.showinfo('Thanks','Thanks')
                        t.destroy()
                        
                    close=Button(p,text='Close Application',bg='Red',command=clsap)
                    close.place(x=350,y=450)                    
                    
                    def clr1():
                        cstidi.delete(0,100)
                        cni.delete(0,100)
                        cadi.delete(0,100)
                        ceidi.delete(0,100)
                        pcidi.delete(0,100)
                        
                    clr=Button(p,text='Clear',command=clr1)
                    clr.place(x=250,y=450)                    
                    
                    
                    def savedata_customer():
                        en1=cstidi.get()
                        en2=pcidi.get()
                        en3=cadi.get()
                        en4=cni.get()
                        en5=ceidi.get() 

                        try:
                            if en2.startswith('PC')!=True or en1.startswith('C')!=True :
                                raise Exception
                            else:
                                s="insert into customer values('%s','%s','%s','%s','%s')"%(en1,en4,en3,en5,en2)
                                try:
                                    cur.execute(s)
        
                                    db.commit()
                                    excustid.append(en1)
                                    messagebox.showinfo('Saved','Data Saved')     
                                    cstidi.delete(0,100)
                                    pcidi.delete(0,100)
                                    cadi.delete(0,100)
                                    cni.delete(0,100)
                                    ceidi.delete(0,100)
                                    p.destroy()
                                except Exception as ex:
                                    messagebox.showinfo('Error',ex)
                        except Exception:
                            messagebox.showinfo('Error',"Product Category ID and Customer ID should starts with 'PC' and 'C'")


                        
                    submit=Button(p,text='Submit',command=savedata_customer)
                    submit.place(x=250,y=400)
                    
                def deletedata_customer():
                    name=simpledialog.askstring("Input","Enter the Customer-ID",parent=p)
                    s="delete from customer where CustID='%s'"%(name)
                    try:
                        cur.execute(s)
                        #Save
                        db.commit()
                        excustid.remove(name)
                        messagebox.showinfo('Delete','Data Deleted')    
                        p.destroy()                      
                    except Exception as ex:
                        messagebox.showinfo('Error',ex)

                submit=Button(p,text='Enter Details',command=enterdetails)
                submit.place(x=150,y=50)

                dlt=Button(p,text='DELETE RECORD',command=deletedata_customer)
                dlt.place(x=350,y=50)

#ENGINEER TABLE
            elif ch==4: 
                p=Toplevel()
                p.geometry("%dx%d"%(width,height))
                p.config(bg='lightblue')
                def enterdetails():
                
                    hd=Label(p,text='Enter the Engineer Details')
                    hd.place(x=100,y=100)
                    hd.config(font=('Helvetica bold',20))
                    
                    eid=Label(p,text='Engineer Id')
                    eid.place(x=100,y=150)
                    eidi=Entry(p,width=40)
                    eidi.place(x=250,y=150)
                    
                    en=Label(p,text='Engineer name')
                    en.place(x=100,y=200)
                    eni=Entry(p,width=40)
                    eni.place(x=250,y=200)
                    
                    ead=Label(p,text='Address')
                    ead.place(x=100,y=250)
                    eadi=Entry(p,width=40)
                    eadi.place(x=250,y=250)
                    
                    eeid=Label(p,text=' Engineer E-Mail Id')
                    eeid.place(x=100,y=300)
                    eeidi=Entry(p,width=50)
                    eeidi.place(x=250,y=300)
                    
                    epn=Label(p,text='Engineer Phone number')
                    epn.place(x=100,y=350)
                    epni=Entry(p,width=40)
                    epni.place(x=250,y=350)
                    
                    
                    pcid=Label(p,text='Product Catgory Id')
                    pcid.place(x=100,y=400)
                    #pcidi=Entry(p,width=40)
                    n = tkinter.StringVar()
                    pcidi = ttk.Combobox(p, width = 27, textvariable = n)
                    pcidi['values']=expcid                    

                    pcidi.place(x=250,y=400)
                                    
                    def close1():
                        messagebox.showinfo('Thanks','Thanks')
                        p.destroy()
                        
                    close=Button(p,text='Back to Main Menu',command=close1)
                    close.place(x=350,y=450)
                    
                    def clsap():
                        messagebox.showinfo('Thanks','Thanks')
                        t.destroy()
                        
                    close=Button(p,text='Close Application',bg='Red',command=clsap)
                    close.place(x=350,y=500)                    
                    
                    def clr1():
                        eidi.delete(0,100)
                        eni.delete(0,100)
                        eadi.delete(0,100)
                        eeidi.delete(0,100)
                        epni.delete(0,100)
                        pcidi.delete(0,100)
                        
                    clr=Button(p,text='Clear',command=clr1)
                    clr.place(x=250,y=500)                    
                    
                    
                    def savedata_engineer():
                        en1=eidi.get()
                        en2=pcidi.get()
                        en3=eadi.get()
                        en4=eni.get() 
                        if epni.get().isalpha():
                            messagebox.showinfo('Error','Phone Number Must be in Digits')
                        else:
                            en5=int(epni.get())
 
                        #en5=int(epni.get())

                        try:
                            if en2.startswith('PC')!=True or en1.startswith('E')!=True :
                                raise Exception
                            else:
                                s="insert into engineers values('%s','%s','%s',%d,'%s')"%(en1,en4,en3,en5,en2)
                                try:
                                    cur.execute(s)
        #Save
                                    db.commit()
                                    exengid.append(en1)
                                    messagebox.showinfo('Saved','Data Saved')
           
                                    eidi.delete(0,100)
                                    pcidi.delete(0,100)
                                    eadi.delete(0,100)
                                    eni.delete(0,100)
                                    epni.delete(0,100)
                                    p.destroy()
                                except Exception as ex:
                                    messagebox.showinfo('Error',ex)
                        except Exception:
                            messagebox.showinfo('Error',"Product Category ID and Engineer ID should starts with 'P' and 'E'")
    
                        
                    submit=Button(p,text='Submit',command=savedata_engineer)
                    submit.place(x=250,y=450)
        
                def deletedata_engineer():
                    name=simpledialog.askstring("Input","Enter the Engineer-ID",parent=p)
                    
                    s="delete from engineers where EngID='%s'"%(name)
                    try:
                        cur.execute(s)
                        #Save
                        db.commit()
                        exengid.remove(name)
                        messagebox.showinfo('Delete','Data Deleted')     
                        p.destroy()
                        
                    except Exception as ex:
                        messagebox.showinfo('Error',ex)

                submit=Button(p,text='Enter Details',command=enterdetails)
                submit.place(x=150,y=50)
                
                dlt=Button(p,text='DELETE RECORD',command=deletedata_engineer)
                dlt.place(x=350,y=50)


            #STAFF TABLE
            elif ch==5: 
                p=Toplevel()
                p.geometry("%dx%d"%(width,height))
                p.config(bg='lightblue')
                def enterdetails():
                    hd=Label(p,text='Enter the Staff Details')
                    hd.place(x=100,y=100)
                    hd.config(font=('Helvetica bold',20))
                    
                    stid=Label(p,text='Staff ID')
                    stid.place(x=100,y=150)
                    stidi=Entry(p,width=40)
                    stidi.place(x=250,y=150)
                    
                    stn=Label(p,text='Staff Name')
                    stn.place(x=100,y=200)
                    stni=Entry(p,width=40)
                    stni.place(x=250,y=200)
                    
                    stad=Label(p,text='Staff Address')
                    stad.place(x=100,y=300)
                    stadi=Entry(p,width=40)
                    stadi.place(x=250,y=300)
                    
                    steid=Label(p,text='Staff Email Id')
                    steid.place(x=100,y=250)
                    steidi=Entry(p,width=40)
                    steidi.place(x=250,y=250)
                    
                    def close1():
                        messagebox.showinfo('Thanks','Thanks')
                        p.destroy()
                        
                    close=Button(p,text='Back to Main Menu',command=close1)
                    close.place(x=350,y=350)

                    def clsap():
                        messagebox.showinfo('Thanks','Thanks')
                        t.destroy()
                        
                    close=Button(p,text='Close Application',bg='Red',command=clsap)
                    close.place(x=350,y=400)
                    
                    def clr1():
                        stidi.delete(0,100)
                        stni.delete(0,100)
                        stadi.delete(0,100)
                        steidi.delete(0,100)
                        
                    clr=Button(p,text='Clear',command=clr1)
                    clr.place(x=250,y=400)                    
                    
                    def savedata_callcenter():
                        en1=stidi.get()
                        en2=stni.get()
                        en3=steidi.get()
                        en4=stadi.get()  
                        
                        try:
                            if en1.startswith('ST')!=True :
                                raise Exception
                            else:
                                s="insert into call_center values('%s','%s','%s','%s')"%(en1,en2,en3,en4)
                                try:
                                    cur.execute(s)
        #Save
                                    db.commit()
                                    exstfid.append(en1)
                                    messagebox.showinfo('Saved','Data Saved')     
                                    stidi.delete(0,100)
                                    stni.delete(0,100)
                                    steidi.delete(0,100)
                                    stadi.delete(0,100)
                                    p.destroy()

                        
                                    
                                except Exception as ex:
                                    messagebox.showinfo('Error',ex)

                        except Exception:
                            messagebox.showinfo('Error',"Staff ID should starts with 'ST'")
                        


                    submit=Button(p,text='Submit',command=savedata_callcenter)
                    submit.place(x=250,y=350)
                    
                
                
                def deletedata_staff():
                    name=simpledialog.askstring("Input","Enter the Staff-ID",parent=p)
                    
                    s="delete from call_center where StaffID='%s'"%(name)
                    try:
                        cur.execute(s)
                        #Save
                        db.commit()
                        exstfid.remove(name)
                        messagebox.showinfo('Delete','Data Deleted')     
                        p.destroy()
                        
                    except Exception as ex:
                        messagebox.showinfo('Error',ex)
                submit=Button(p,text='Enter Details',command=enterdetails)
                submit.place(x=150,y=50)

                dlt=Button(p,text='DELETE RECORD',command=deletedata_staff)
                dlt.place(x=350,y=50)

            #Complain Table/CAll Assign Table
            elif ch==6: 
                p=Toplevel()
                p.geometry("%dx%d"%(width,height))
                p.config(bg='lightblue')

                piechart='select PCATID,CHARGES from Call_assign'
                #cur=db.cursor()
                cur.execute(piechart)
                n=[]
                s=[]
                data=cur.fetchall()
                for r in data:
                    n.append(r[0])
                    s.append(r[1])
                col=['r','b','g']
                # plt.pie(s,labels=n,colors=col)
                # plt.show()
                plt.bar(n,s)
                plt.xticks(n,s)
                plt.show()

                today = date.today()
                def enterdetails():
                    hd=Label(p,text='Enter the Details')
                    hd.place(x=100,y=100)
                    hd.config(font=('Helvetica bold',20))
                    
                    date=Label(p,text='Date (YYYY-MM-DD)')
                    date.place(x=100,y=150)
                    date=Label(p,text=today)
                    date.place(x=250,y=150)
                    
                    
                    stid=Label(p,text='Staff ID')
                    stid.place(x=100,y=200)
                    #stidi=Entry(p,width=40)

                    n = tkinter.StringVar()
                    global stidi
                    stidi = ttk.Combobox(p, width = 27, textvariable = n)
                    stidi['values']=exstfid
                    stidi.place(x=250,y=200)
                    
                    eid=Label(p,text='Engineer Id')
                    eid.place(x=100,y=250)
                    #eidi=Entry(p,width=40)
                    nen = tkinter.StringVar()
                    global eidi
                    eidi = ttk.Combobox(p, width = 27, textvariable = nen)
                    eidi['values']=exengid
                    eidi.place(x=250,y=250)
                    
                    cstid=Label(p,text='Customer Id')
                    cstid.place(x=100,y=300)
                    #cstidi=Entry(p,width=40)
                    ncust = tkinter.StringVar()
                    global cstidi
                    cstidi = ttk.Combobox(p, width = 27, textvariable = ncust)
                    cstidi['values']=excustid
                    cstidi.place(x=250,y=300)
                    
                    pcid=Label(p,text='Product Category ID')
                    pcid.place(x=100,y=350)
                    #pcidi=Entry(p,width=40)
                    npcat = tkinter.StringVar()
                    global pcidi
                    pcidi = ttk.Combobox(p, width = 27, textvariable = npcat)
                    pcidi['values']=expcid

                    pcidi.place(x=250,y=350)
                    
                    cgt=Label(p,text='Charges')
                    cgt.place(x=100,y=400)
                    current_value = StringVar(value=0)
                    global cgti
                    cgti=Entry(p,width=40,textvariable=current_value)
                    cgti.place(x=250,y=400)
                    
                    sts=Label(p,text='Status')
                    sts.place(x=100,y=450)
                    current_value1 = StringVar(value=0)
                    stsi=Spinbox(p,from_=0,to=1,textvariable=current_value1,wrap=True)
                    stsi.place(x=250,y=450)
                    
                    def close1():
                        messagebox.showinfo('Thanks','Thanks')
                        p.destroy()
                        
                    close=Button(p,text='Back to Main Menu',command=close1)
                    close.place(x=350,y=500)
                    
                    def clsap():
                        messagebox.showinfo('Thanks','Thanks')
                        t.destroy()
                        
                    close=Button(p,text='Close Application',bg='Red',command=clsap)
                    close.place(x=350,y=550)                    
                    
                    def clr1():
                        stidi.delete(0,100)
                        eidi.delete(0,100)
                        cstidi.delete(0,100)
                        pcidi.delete(0,100)
                        cgti.delete(0,100)
                        stsi.delete(0,100)
                        
                        
                    clr=Button(p,text='Clear',command=clr1)
                    clr.place(x=250,y=550)


                    def savedata_CallAssign():
                        en1=stidi.get()
                        en2=eidi.get()
                        en3=cstidi.get()
                        en4=pcidi.get()
                        en5=today
                        global cplnid
                        cplnid=code()
                        if cgti.get().isalpha():
                            messagebox.showinfo('Error','Charges Must be in Digits')
                        else:
                            en6=int(cgti.get())
                        #en6=int(cgti.get())
                        if stsi.get().isalpha():
                            messagebox.showinfo('Error','Status Must be in 0 or 1')
                        else:
                            en7=int(stsi.get())
                        #en7=int(cgtii.get()) 
                        s="insert into Call_assign values('%s','%s','%s','%s',%d,%d,'%s','%s')"%(en1,en2,en3,en4,en6,en7,en5,cplnid)
                        try:
                            cur.execute(s)
    #Save
                            db.commit()
                            messagebox.showinfo('Saved','Data Saved')
                            email()     
                            stidi.delete(0,100)
                            eidi.delete(0,100)
                            cstidi.delete(0,100)
                            pcidi.delete(0,100)                        
                            cgti.delete(0,100)
                            stsi.delete(0,100)
                            p.destroy()
                        except Exception as ex:
                            messagebox.showinfo('Error',ex)
                        
                    submit=Button(p,text='Submit',command=savedata_CallAssign)
                    submit.place(x=250,y=500)
                

                
                
                def dltrec():
                    name=simpledialog.askstring("Input","Enter the Product Category ID",parent=p)
    
                    s="delete from Call_assign where PCatId='%s'"%(name)
                    try:
                        cur.execute(s)
                        #Save
                        db.commit()
                        messagebox.showinfo('Delete','Data Deleted')     
                        p.destroy()
                        
                    except Exception as ex:
                        messagebox.showinfo('Error',ex)
        
                submit=Button(p,text='Enter Details',command=enterdetails)
                submit.place(x=150,y=50)

                dlt=Button(p,text='DELETE RECORD',command=dltrec)
                dlt.place(x=350,y=50)

            else:
                messagebox.showinfo('wrong choice','please try again')

        aa=IntVar()
        p=Toplevel()
        p.geometry("%dx%d"%(width,height))
        p.config(bg='lightblue')
        r1=Radiobutton(p,text='Enter New Product Category Details',bg='royalblue',variable=aa,value=0,command=choice)
        r2=Radiobutton(p,text='Enter New Product Details',bg='royalblue',variable=aa,value=1,command=choice)
        r3=Radiobutton(p,text='Enter Service Details',bg='royalblue',variable=aa,value=2,command=choice)
        r4=Radiobutton(p,text='Enter Customer Details',bg='royalblue',variable=aa,value=3,command=choice)
        r5=Radiobutton(p,text='Enter Engineer Details',bg='royalblue',variable=aa,value=4,command=choice)
        r6=Radiobutton(p,text='Enter Staff Details',bg='royalblue',variable=aa,value=5,command=choice)
        r7=Radiobutton(p,text='Enter Complain Details',bg='royalblue',variable=aa,value=6,command=choice)
        
        adh=Label(p,text='Add/Delete Details')
        adh.config(font=('Helvetica bold',20))
        adh.place(x=400,y=150)
        
        r1.place(x=400,y=200)
        r2.place(x=400,y=250)
        r3.place(x=400,y=300)
        r4.place(x=400,y=350)
        r5.place(x=400,y=400)
        r6.place(x=400,y=450)
        r7.place(x=400,y=500)
        
        sh=Label(p,text='Search Details')
        sh.config(font=('Helvetica bold',20))
        sh.place(x=900,y=150)
        
        def productsearch():
            srh=Toplevel()
            srh.geometry("%dx%d"%(width,height))
            srh.config(bg='lightblue')
            
            sph=Label(srh,text='Search Details')
            sph.config(font=('Helvetica bold',20))
            sph.place(x=0,y=50)
            
            aa=Label(srh,text='Select the Product-Id')
            aa.place(x=50,y=100)
            
            
            n = tkinter.StringVar()
            srcpid = ttk.Combobox(srh, width = 27, textvariable = n)
            srcpid['values']=expid
            srcpid.place(x=50,y=150)
            

            
            def dis():
                spid=srcpid.get()
                cursor = db.cursor()        
                srchdata= "select PID,NAME,COST from product where PID='%s' "%(spid)
                try:
                    A=[]
                    cursor.execute(srchdata)
                    data=cursor.fetchone()
                    A.insert(0,data[0])
                    A.insert(1,data[1])
                    A.insert(2,data[2])
                    messagebox.showinfo ("Details",A)
                    srh.destroy()
                    
                    
                except:
                    messagebox.showinfo ("Error","Error: unable to Find")
                    srh.destroy()

            psb=Button(srh,text='Search',bg='royalblue',command=dis)
            psb.place(x=50,y=200)
                
            srh.mainloop()



        pds=Button(p,text='Product Details',bg='royalblue',command=productsearch)
        pds.place(x=900,y=350)        

        def engsearch():
            srh=Toplevel()
            srh.geometry("%dx%d"%(width,height))
            srh.config(bg='lightblue')
            
            sph=Label(srh,text='Search Details')
            sph.config(font=('Helvetica bold',18))
            sph.place(x=0,y=50)
            
            aa=Label(srh,text='Select the Engineer-Id')
            aa.place(x=50,y=100)
            
            
            n = tkinter.StringVar()
            srcpid = ttk.Combobox(srh, width = 27, textvariable = n)
            srcpid['values']=exengid
            srcpid.place(x=50,y=150)
            

            
            def dis():
                spid=srcpid.get()
                cursor = db.cursor()        
                srchdata= "select ENGID,ENAME,ADDRESS,PHONE from engineers where ENGID='%s' "%(spid)
                try:
                    A=[]
                    cursor.execute(srchdata)
                    data=cursor.fetchone()
                    A.insert(0,data[0])
                    A.insert(1,data[1])
                    A.insert(2,data[2])
                    A.insert(3,data[3])
                    messagebox.showinfo ("Details",A)

                    srh.destroy()                    
                    
                except:
                    messagebox.showinfo ("Error","Error: unable to Find")
                    srh.destroy()

            psb=Button(srh,text='Search',bg='royalblue',command=dis)
            psb.place(x=50,y=200)
                
            srh.mainloop()

        
        eds=Button(p,text='Engineer Details',bg='royalblue',command=engsearch)
        eds.place(x=900,y=450)        

        def customersearch():
            srh=Toplevel()
            srh.geometry("%dx%d"%(width,height))
            srh.config(bg='lightblue')
            
            sph=Label(srh,text='Search Details')
            sph.config(font=('Helvetica bold',20))
            sph.place(x=50,y=50)
            
            aa=Label(srh,text='Select the Customer-Id')
            aa.place(x=50,y=100)
            
            n = tkinter.StringVar()
            srcpid = ttk.Combobox(srh, width = 27, textvariable = n)
            srcpid['values']=excustid
            srcpid.place(x=50,y=150)
            

            
            def dis():
                spid=srcpid.get()
                cursor = db.cursor()        
                srchdata= "select CUSTID,NAME,ADDRESS from customer where CUSTID='%s' "%(spid)
                try:
                    A=[]
                    cursor.execute(srchdata)
                    data=cursor.fetchone()
                    A.insert(0,data[0])
                    A.insert(1,data[1])
                    A.insert(2,data[2])
                    messagebox.showinfo ("Details",A)
                    srh.destroy()
                    
                except:
                    messagebox.showinfo ("Error","Error: unable to Find")
                    srh.destroy()

            psb=Button(srh,text='Search',bg='royalblue',command=dis)
            psb.place(x=50,y=200)
                
            srh.mainloop()

        
        cds=Button(p,text='Customer Details',bg='royalblue',command=customersearch)
        cds.place(x=900,y=250)   
        
    else:
        messagebox.showinfo('wrong password','please try again')
        


       
def clear():
    adi.delete(0,100)
    passi.delete(0,100)
    
def clsap():
   messagebox.showinfo('Thanks','Thanks')
   t.destroy()
                        
close=Button(t,text='Close Application',bg='Red',command=clsap)
close.place(x=580,y=350) 
close.config(font=('Helvetica bold',12,'bold'))
    

submit=Button(t,text='Submit',bg='Green', command=check,width=8,height=1)
submit.place(x=390,y=350)
submit.config(font=('Helvetica bold',12,'bold'))


cnl=Button(t,text='Clear',bg='White',command=clear)
cnl.place(x=500,y=350)
cnl.config(font=('Helvetica bold',12,'bold'))

t.mainloop()
db.close()