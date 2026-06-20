def get_middle_element(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    
    n = len(numbers)
    middle_index = n // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    try:
        print(get_middle_element(sample_numbers))
    except ValueError as e:
        print(e)