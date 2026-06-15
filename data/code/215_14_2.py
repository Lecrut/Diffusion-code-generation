import sys
if __name__ == '__main__':
    input_line = "10 5 20 8 15"
    numbers = list(map(int, input_line.split()))
    if numbers:
        maximum = max(numbers)
        print(maximum)