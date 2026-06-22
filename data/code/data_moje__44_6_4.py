def calculate_mean(numbers):
    if not numbers:
        return None
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = calculate_mean(sample_numbers)
    print(result)
    empty_list = []
    result_empty = calculate_mean(empty_list)
    print(result_empty)