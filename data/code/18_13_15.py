def get_central_element(array):
    if not array:
        return None
    index = len(array) // 2
    return array[index]

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [1, 2, 3, 4, 5, 6]
    print(get_central_element(sample_odd))
    print(get_central_element(sample_even))
    print(get_central_element([]))