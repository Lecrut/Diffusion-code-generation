def find_max_number(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == '__main__':
    input_data = [10, 5, 22, 8, 30, 15]
    largest_number = find_max_number(input_data)
    print(largest_number)