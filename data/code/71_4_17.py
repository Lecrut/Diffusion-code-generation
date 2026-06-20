def get_middle_element(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    n = len(numbers)
    middle_index = n // 2
    return numbers[middle_index]

if __name__ == '__main__':
    try:
        numbers = [10, 20, 30, 40, 50]
        print(get_middle_element(numbers))
    except ValueError as e:
        print(e)