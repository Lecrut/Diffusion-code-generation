import sys
if __name__ == '__main__':
    numbers_input = "10 20 30 40 50"
    numbers = list(map(int, numbers_input.split()))
    total_sum = sum(numbers)
    print(total_sum)