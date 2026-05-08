def calculate_sum(numbers):
    return sum(numbers)
if __name__ == '__main__':
    large_list = list(range(1000000))
    result = calculate_sum(large_list)
    print(result)