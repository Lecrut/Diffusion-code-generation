def find_minimum(numbers):
    current_min = numbers[0]
    for num in numbers[1:]:
        if num < current_min:
            current_min = num
    return current_min

if __name__ == '__main__':
    sample_values = [42, 17, 5, 88, -3, 99, 12]
    result = find_minimum(sample_values)
    print(result)