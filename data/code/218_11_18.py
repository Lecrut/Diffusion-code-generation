def find_min(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
    return min_num

if __name__ == '__main__':
    sample_data1 = [5, 2, 8, 1, 9]
    print(f"Minimum of {sample_data1}: {find_min(sample_data1)}")