def user_greeting():
    print("Hi")

def asking_user_name_and_greet():
    user_name=input("what is your name?")
    print("Hi",user_name)

def user_calculation_choice():
    print("pick one operation")
    user_calc_operation_choice=input("+ / - / * / /")
    add_number_to_calc=int(input("pick first number"))
    add_second_number_to_calc=int(input("pick second_number"))
    if user_calc_operation_choice == "+":
        print("the sum is",add_number_to_calc + add_second_number_to_calc)
    if user_calc_operation_choice == "-":
        print("the sum is",add_number_to_calc - add_second_number_to_calc)
    if user_calc_operation_choice == "*":
        print("the sum is",add_number_to_calc * add_second_number_to_calc)
    if user_calc_operation_choice == "/":
        print("the sum is",add_number_to_calc / add_second_number_to_calc)
    if  add_second_number_to_calc == 0 :
        print("division by zero is an error")

user_greeting()
asking_user_name_and_greet()
user_calculation_choice()
