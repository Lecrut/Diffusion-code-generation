import sys
if __name__ == '__main__':
    input_data = "10 25"
    parts = input_data.split()
    if len(parts) >= 2:
        num1 = int(parts[0])
        num2 = int(parts[1])
        sum1 = num1
        sum2 = num2
        if sum1 > sum2:
            print(f"Sum of {num1} is larger than the sum of {num2}")
        elif sum2 > sum1:
            print(f"Sum of {num2} is larger than the sum of {num1}")
        else:
            print(f"The sums of {num1} and {num2} are equal")
    else:
        print("Error: Insufficient input provided.")