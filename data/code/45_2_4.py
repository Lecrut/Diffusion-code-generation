def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

if __name__ == '__main__':
    sample_list = [3.5, 1.2, 9.8, -4.1, 0.0]
    result = find_minimum(sample_list)
    print(result)
    try:
        find_minimum([])
    except ValueError as e:
        print(e)