import sys
if __name__ == '__main__':
    input_line = "10 5 20 3"
    numbers = list(map(int, input_line.split()))
    maximum = max(numbers)
    print(maximum)