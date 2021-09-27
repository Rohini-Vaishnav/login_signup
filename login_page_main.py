import json
def sign_up():
    dic={}
    username=input("enter the user name :")
    password1=input("enter the passward :")
    password2=input("confrom your passward :")
    if password1!=password2:
        print("both passward are not same")
    else:
        if "@" in password2 or "$" in password2 or "#" in password2:
            if "0" or "9" in password2:
                if "A" or "Z" in password2:
                    with open("main.json","r") as a:
                        all_data = json.load(a)
                    i=0
                    while i<len(all_data["user"]):
                        a=(all_data["user"][i])
                        if a["username"]==username:
                            print("**************** alredy exist *********************")
                            break
                        i=i+1 
                    else:
                        dic["username"]=username
                        dic["passward"]=password1
                        all_data["user"].append(dic)

                        with open("main.json","w") as w:
                            json.dump(all_data,w,indent=4)
                        print()
                        print("congress",username,"your singnup sucessfully")
                        print()
                        details=input("enter the discreption:---")
                        Birthday_date=input("enter the birthday date:---")
                        Hobbis=input("enter the hobbis:---")
                        Gender=input("enter the gender:---")
                        dic_bio={}
                        dic_bio["Descreption"]=details
                        dic_bio["dob"]=Birthday_date
                        dic_bio["Hobbis"]=Hobbis
                        dic_bio["Gender"]=Gender
                        dic["profile"]=dic_bio
                        with open("main.json","w") as w:
                            json.dump(all_data,w,indent=4)
                else:
                    print("atlist password should contain one apper charcter....")
            else:
                print("atlist password should contain one number...")                
        else:
            print("atlist password should contain one special charcter....")
def login():
    username_l=input("enter the user name for login :")
    password_l=input("enter the password for login :")
    j_data=open("main.json", "r")
    a_data=json.load(j_data)
    print(a_data)
    j_data.close() 
    i=0
    while i<len(a_data["user"]):
        a=(a_data["user"][i])
        if a["username"]==username_l:
                print(username_l, "you are logged In Successfully")
                print("***************************")
                print("profile")
                print("Username:",username_l)
                print("Gender:", a['profile']['Gender'])
                print("Bio:", a['profile']["Descreption"])
                print("Hobbis:", a['profile']['Hobbis'])
                print("Dob:", a['profile']['dob'])
                break
        i=i+1
    else:
        print("invalid username")
def main():
    print("print 's' for sign_up and 'l' for login ")
    user_want=input("what you want to do :")
    if user_want=='s':
        sign_up()
    elif user_want=='l':
        login()
    else:
        print("print s or l")
main()
