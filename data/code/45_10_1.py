def find_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    minimum_value = numbers[0]
    for num in numbers[1:]:
        if num < minimum_value:
            minimum_value = num
    return minimum_value

if __name__ == '__main__':
    sample_list = [34, 12, 5, 89, 3, 45, 2]
    result = find_minimum(sample_list)
    print(result)