def find_max(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for i in range(1, len(numbers)):
        current_num = numbers[i]
        if current_num > max_val:
            max_val = current_num
    return max_val
if __name__ == '__main__':
    sample_list = [34.6, -20.2, 54.8, 79.1, 3.8]
    result = find_max(sample_list)
    print(result)