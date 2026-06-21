def get_first_element(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return numbers[0]

if __name__ == '__main__':
    sample_list = [42, 7, 19, 33]
    first_element = get_first_element(sample_list)
    print(first_element)