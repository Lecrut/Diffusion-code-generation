import sys
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    numbers = list(map(int, input_data.split()))
    total_sum = sum(numbers)
    print(total_sum)