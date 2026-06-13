import sys
if __name__ == '__main__':
    input_line = "10 5 22 8 1"
    try:
        numbers = list(map(int, input_line.split()))
        if numbers:
            smallest = min(numbers)
            print(smallest)
        else:
            print("The input line contained no numbers.")
    except ValueError:
        print("Error: Input contains non-integer values.")