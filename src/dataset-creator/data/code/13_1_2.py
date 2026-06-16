def find_max_element(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for i in range(1, len(numbers)):
        current_value = numbers[i]
        if current_value > max_val:
            max_val = current_value
    return max_val
if __name__ == '__main__':
    sample_list = [34, 78, 25, 90, -15, 67]
    result = find_max_element(sample_list)
    print(result)