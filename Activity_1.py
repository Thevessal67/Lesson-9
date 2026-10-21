print("="*40)
print("welcome to the rider builder!")
print("="*40)
print()
print("step 1: choose your vehicle")
print("1. Bike")
print("2. Car")
print()
choice=int(input("Enter your choice (1 or 2): "))
if choice==1:
    print("You have chosen Bike.")
    print("step 2: choose your bike type")
    print("1. Mountain Bike")
    print("2. Scooty")
    bike_choice=int(input("Enter your choice (1 or 2): "))
    if bike_choice==1:
        print("You have chosen Mountain Bike.")
        print("minimum speed: 30 km/h")
        print("best for off-road trails and rough terrains.")
    elif bike_choice==2:
        print("You have chosen Scooty.")
        print("minimum speed: 25 km/h")
        print("best for urban commuting and short distances.")
    else:
        print("Invalid choice.")
elif choice==2:
    print("You have chosen Car.")
    print("step 2: choose your car type")
    print("1. Sedan")
    print("2. SUV")
    car_choice=int(input("Enter your choice (1 or 2): "))
    if car_choice==1:
        print("You have chosen Sedan.")
        print("minimum speed: 100 km/h")
        print("passengers: 4")
        print("best for city driving and long-distance travel.")
    elif car_choice==2:
        print("You have chosen SUV.")
        print("minimum speed: 60 km/h")
        print("passengers: 6")
        print("best for off-road adventures and family trips.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice, please choose either 1 or 2.")
print("="*40)
print("Thank you for using the rider builder!")
print("enjoy your ride!")
print("="*40)