import sys
if __name__ == '__main__':
    input_data = "15 3 8 22 1"
    numbers = list(map(int, input_data.split()))
    if numbers:
        minimum = min(numbers)
        print(minimum)