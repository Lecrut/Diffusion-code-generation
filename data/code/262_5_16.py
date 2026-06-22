def find_min_max(numbers):
    min_num = max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num

if __name__ == '__main__':
    sample_numbers = [3456789, 1234567, 9876543, 2345678, 6789012]
    print(find_min_max(sample_numbers))