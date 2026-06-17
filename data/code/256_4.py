import sys
if __name__ == '__main__':
    input_line = "10 5 20 3"
    numbers = [float(x) for x in input_line.split()]
    if not numbers:
        print("No numbers provided.")
    else:
        minimum = min(numbers)
        maximum = max(numbers)
        range_val = maximum - minimum
        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")
        print(f"Range: {range_val}")