import sys
if __name__ == '__main__':
    input_data = "10 5 22 8 35 1"
    numbers = [int(x) for x in input_data.split()]
    if numbers:
        maximum = max(numbers)
        print(maximum)
    else:
        print("No numbers provided")