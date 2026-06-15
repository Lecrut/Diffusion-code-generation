def calculate_sum(numbers):
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total
if __name__ == '__main__':
    sample_list = [1, 5, 10, -3, 8]
    result = calculate_sum(sample_list)
    print(result)
    empty_list = []
    result_empty = calculate_sum(empty_list)
    print(result_empty)