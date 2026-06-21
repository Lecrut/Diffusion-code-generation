def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4, 8, 7, 6]
    print(find_max(sample_list))