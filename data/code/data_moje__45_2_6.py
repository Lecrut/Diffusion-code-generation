def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_numbers = [3.5, 1.2, 4.8, 2.1, 5.3]
    result = find_minimum(sample_numbers)
    print(result)

    empty_list = []
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(str(e))