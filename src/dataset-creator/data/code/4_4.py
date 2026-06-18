def get_valid_numbers():
    while True:
        try:
            num1 = int(input("Enter the first integer: "))
            num2 = int(input("Enter the second integer: "))
            num3 = int(input("Enter the third integer: "))
            return num1, num2, num3
        except ValueError:
            print("Invalid input. Please enter integers only.")
if __name__ == '__main__':
    try:
        n1 = 5
        n2 = 10
        n3 = 15
        sum_result = n1 + n2 + n3
        print(f"The sum of {n1}, {n2}, and {n3} is: {sum_result}")
    except Exception as e:
        print(f"An error occurred: {e}")