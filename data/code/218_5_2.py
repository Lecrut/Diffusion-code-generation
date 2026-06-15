import sys
if __name__ == '__main__':
    input_data = "10 5 22 3 18"
    numbers = list(map(int, input_data.split()))
    if numbers:
        minimum = min(numbers)
        print(minimum)