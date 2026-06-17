import sys
if __name__ == '__main__':
    input_line = "10 5 20 15 30"
    numbers = [float(x) for x in input_line.split()]
    if numbers:
        print(f"Minimum: {min(numbers)}")
        print(f"Maximum: {max(numbers)}")
    else:
        print("No numbers provided")