def get_first_element(numbers):
    if not numbers:
        return None
    return numbers[0]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = []
    print(get_first_element(sample_list_1))
    print(get_first_element(sample_list_2))