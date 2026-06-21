def get_first_element(numbers):
    if not numbers:
        return None
    return numbers[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    print(get_first_element(sample_list))
    empty_list = []
    print(get_first_element(empty_list))