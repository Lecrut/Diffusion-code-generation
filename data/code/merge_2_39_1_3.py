def find_max(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for i in range(1, len(numbers)):
        current_number = numbers[i]
        if current_number > max_value:
            max_value = current_number
    return max_value
if __name__ == '__main__':
    sample_list = [34.67, -50.2, 12.78, 98.45, -10.0]
    result = find_max(sample_list)
    print(result)