def find_minimum(numbers):
    if not numbers:
        return None
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value
if __name__ == '__main__':
    sample_list = [4, 9, 1, 3, 5, 7, 2]
    print(find_minimum(sample_list))