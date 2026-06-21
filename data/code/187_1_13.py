def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2, 9, 4]
    print(find_max(sample_numbers))