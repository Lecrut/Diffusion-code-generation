def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == '__main__':
    sample_values = [12, 7, 19, 3, 15, 8]
    print(find_max(sample_values))