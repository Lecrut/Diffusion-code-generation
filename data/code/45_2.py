def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    current_min = numbers[0]
    for num in numbers:
        if num < current_min:
            current_min = num
    return current_min

if __name__ == '__main__':
    sample_list = [3.14, 1.59, 2.65, 3.58, 9.79]
    result = find_minimum(sample_list)
    print(result)