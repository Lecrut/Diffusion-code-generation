def find_max_element(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(find_max_element(sample_values))