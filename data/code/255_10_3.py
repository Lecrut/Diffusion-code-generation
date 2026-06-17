import sys
if __name__ == '__main__':
    input_data = "10 5 22 8 30 1"
    numbers = list(map(int, input_data.split()))
    if numbers:
        maximum = max(numbers)
        print(maximum)
    else:
        print("List is empty")