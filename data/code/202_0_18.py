def find_max_number(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == '__main__':
    sample_data = [12, 45, 78, 34, 90, 23]
    result = find_max_number(sample_data)
    print(result)