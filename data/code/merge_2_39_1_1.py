def find_max_iterative(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for i in range(1, len(numbers)):
        current_number = numbers[i]
        if current_number > max_value:
            max_value = current_number
    return max_value
if __name__ == '__main__':
    sample_list = [34, 78, 90, -5, 12, 67, 45, 23]
    result = find_max_iterative(sample_list)
    print(result)