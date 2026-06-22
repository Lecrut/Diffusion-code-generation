def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_data = [3.5, 1.2, 4.8, 0.1, 9.9, 0.1, -5.3]
    print(find_minimum(sample_data))
    empty_data = []
    try:
        find_minimum(empty_data)
    except ValueError as e:
        print(e)