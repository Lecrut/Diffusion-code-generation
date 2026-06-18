def find_max(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for i in range(1, len(numbers)):
        current = numbers[i]
        if current > max_value:
            max_value = current
    return max_value
if __name__ == '__main__':
    sample_list = [34, 78, 25, 90, -10, 67, 45, 8]
    result = find_max(sample_list)
    print(result)