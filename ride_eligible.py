def check_ride_eligibility():
    # Step 2: Enter the height of the applicant
    height = float(input("Enter the height of the applicant in cm: "))

    # Step 3: Check whether the height is greater than 120cm
    if height <= 120:
        # Step 4: If NO, return and display ‘You cannot ride’
        print('You cannot ride')
    else:
        # Step 5: If YES, display ‘You can ride’
        print('You can ride')

        # Step 6: Enter the age of the applicant
        age = int(input("Enter the age of the applicant: "))

        # Step 7-9: Determine the price based on age
        if age < 12:
            print('You will pay $5')
        elif 12 <= age <= 18:
            print('You will pay $7')
        else:
            print('You will pay $12')

    # Step 10: End
    print("End of program")

# Start the program
check_ride_eligibility()
