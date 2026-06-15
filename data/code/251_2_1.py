import sys
if __name__ == '__main__':
    input_data = "42 10 99 3 56"
    numbers = list(map(int, input_data.split()))
    largest = max(numbers)
    print(largest)