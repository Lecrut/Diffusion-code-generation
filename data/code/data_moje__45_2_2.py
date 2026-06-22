def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [3.5, 1.2, 9.8, 0.5, 4.1]
    print(find_minimum(sample_list))
    empty_list = []
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(e)