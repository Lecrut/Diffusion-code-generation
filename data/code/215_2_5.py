import sys
if __name__ == '__main__':
    input_line = "10 5 22 8 30"
    try:
        numbers = list(map(int, input_line.split()))
        if numbers:
            maximum = max(numbers)
            print(maximum)
        else:
            print("No numbers provided")
    except ValueError:
        print("Invalid input: Please ensure all inputs are integers separated by spaces.")