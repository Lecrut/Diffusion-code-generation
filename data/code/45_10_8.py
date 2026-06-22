def find_minimum(numbers):
    current_min = numbers[0]
    for num in numbers[1:]:
        if num < current_min:
            current_min = num
    return current_min

if __name__ == '__main__':
    sample_list = [34, -12, 0, 56, -89, 23]
    result = find_minimum(sample_list)
    print(result)