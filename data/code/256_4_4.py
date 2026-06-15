import sys
if __name__ == '__main__':
    input_line = "10 5 20 3"
    numbers = [float(x) for x in input_line.split()]
    print(f"Minimum: {min(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Range: {max(numbers) - min(numbers)}")