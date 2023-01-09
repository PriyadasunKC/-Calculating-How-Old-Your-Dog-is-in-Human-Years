import traceback

def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
    
        if d_age < 0:
            print("Invalid!,You enter negative! age")
        else:
            if d_age == 1:
                human_age = d_age * 15
                print("The given dog age {} is {} in human years.".format(int(d_age),"%.1f" % human_age))
            elif (d_age > 1 and d_age <= 2):
                human_age = d_age * 12
                print("The given dog age {} is {} in human years.".format(int(d_age),"%.1f" % human_age))
            elif (d_age > 2 and d_age <= 3):
                human_age = d_age * 9.3
                print("The given dog age {} is {} in human years.".format(int(d_age),"%.1f" % human_age))
            elif (d_age > 3 and d_age <= 4):
                human_age = d_age * 8
                print("The given dog age {} is {} in human years.".format(int(d_age),"%.1f" % human_age))
            elif (d_age > 4 and d_age <= 5):
                human_age = d_age * 7.2
                print("The given dog age {} is {} in human years.".format(int(d_age),"%.1f" % human_age))
            else:
                human_age = (5 * 7.2) + ((d_age - 5) * 7)
                print("The given dog age {} is {} in human years.".format(int(d_age),"%.1f" % human_age))
    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
        print("Invalid ! input")
    
calculator() # This line calls the calculator function