def find_minimum(numbers):
    current_min = numbers[0]
    for num in numbers[1:]:
        if num < current_min:
            current_min = num
    return current_min

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_minimum(sample_list)
    print(result)