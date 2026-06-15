def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    result = calculate_sum(sample_list)
    print(result)