def get_middle_element(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    n = len(numbers)
    middle_index = n // 2
    return numbers[middle_index]

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    try:
        middle_element = get_middle_element(numbers)
        print(middle_element)
    except ValueError as e:
        print(e)