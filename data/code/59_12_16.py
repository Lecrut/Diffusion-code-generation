def find_middle_item(numbers):
    n = len(numbers)
    if n == 0:
        return None
    middle_index = n // 2
    if n % 2 == 1:
        return numbers[middle_index]
    else:
        return (numbers[middle_index - 1] + numbers[middle_index]) // 2

if __name__ == '__main__':
    sample_data = [3, 7, 2, 5, 8]
    result = find_middle_item(sample_data)
    print(result)