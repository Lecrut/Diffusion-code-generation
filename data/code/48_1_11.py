def find_largest_number(numbers):
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_numbers = [15, 42, 8, 99, 23, 56, 101, 33, 7]
    result = find_largest_number(sample_numbers)
    print(result)