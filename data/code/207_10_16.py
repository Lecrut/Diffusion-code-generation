def find_max_element(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_values = [4, 9, 2, 7, 5, 11, 3]
    print(find_max_element(sample_values))