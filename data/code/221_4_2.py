import sys
if __name__ == '__main__':
    input_data = "10 25 5"
    numbers = list(map(int, input_data.split()))
    print(*numbers)