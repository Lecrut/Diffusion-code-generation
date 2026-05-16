import sys
def calculate_difference(weight1, weight2):
    return abs(weight1 - weight2)
if __name__ == '__main__':
    weight1 = 50.5
    weight2 = 120.75
    try:
        weight1 = float(input("Enter the first weight: "))
        weight2 = float(input("Enter the second weight: "))
        if weight1 == 0 and weight2 == 0:
            print("Both weights are zero. Difference is 0.")
        else:
            difference = calculate_difference(weight1, weight2)
            print(f"The simple difference between {weight1} and {weight2} is: {difference}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for the weights.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")