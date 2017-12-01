import os
while True:
        os.system('clear')
        print ("Converter Application")
        print ("\nEnter 1. Temperature Converter")
        print ("Enter 2. Currency Converter");
        print ("Enter 3. Mile / Kilometer Converter")
        print ("ENter 4. Inch / Centimeter Converter")
        choice = int(input ("\nWhich conversion do you want?"))
        if choice == 1:
            os.system('clear')
            print ("Type 1 to Convert from Ferienhiet to Celcius.")
            print ("Type 2 to convert from Celcius to Fereinheiet.")
            conversion = int(input ("\nConverion: "))
            os.system('clear')
            if conversion == 1:
                temp = float(input("Enter the Temperature in Ferienhiet: "))
                final = (temp - 32) * 5/9
                final = round(final,2)
                print ("The temperature is equal to {} Celcius.".format(final))
            elif conversion == 2:
                temp = float(input ("Enter the Temperature in Celcius: "))
                final = temp * 9/5 + 32
                final = round(final,2)
                print ("The temperature is equal to {} Ferienhiet.".format(final))
            else:
                print("Invalid entry.")

        elif choice == 2:
            os.system('clear')
            print ("Type 1 to Convert from Dollar to Kwacha.")
            print ("Type 2 to convert from Kwacha to Dollar.")
            conversion = int(input ("\nConverion: "))
            os.system('clear')
            if conversion == 1:
                value = float(input ("Enter the Currency in Dollars: "))
                final = (value * 10.09)
                final = round(final,2)
                print ("The Currency is equal to {} Kwachas.".format(final))
            elif conversion == 2:
                value = float(input ("Enter the Currency in Kwachas: "))
                final = (value / 10.09)
                final = round(final,2)
                print ("The Currency is equal to {} Dollars.".format(final))
            else:
                print("Invalid entry.")

        elif choice == 3:
            os.system('clear')
            print ("Type 1 to Convert from Mile to Kilometer.")
            print ("Type 2 to convert from Kilometer to Mile.")
            conversion = int(input ("\nConverion: "))
            os.system('clear')
            if conversion == 1:
                value = float(input ("Enter the Distance in Miles: "))
                final = vaule * 1.60934
                final = round(final,2)
                print ("The Distance is equal to {} Kilometers.".format(final))
            elif conversion == 2:
                value = float(input ("Enter the Distance in Kilometers: "))
                final = value / 1.60934
                final = round(final,2)
                print ("The Distance is equal to {} Miles.".format(final))
            else:
                print("Invalid entry.")

        elif choice == 4:
            os.system('clear')
            print ("Type 1 to Convert from Inch to Centimeter.")
            print ("Type 2 to convert from Centimeter to Inch.")
            conversion = int(input ("\nConverion: "))
            os.system('clear')
            if conversion == 1:
 
                value = float(input ("Enter the Distance in Inches: "))
                final = value * 2.54
                final = round(final,2)
                print ("The Distance is equal to {} Centimeters.".format(final))
            elif conversion == 2:
                value = float (input ("Enter the Distance in Centimeters: "))
                final = value / 2.54
                final = round(final,2)
                print ("The Distance is equal to {} Inches.".format(final))
            else:
                print("Invalid entry.")
        input("\nPress ENTER to try again.")
