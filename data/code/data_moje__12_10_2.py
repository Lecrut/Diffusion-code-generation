def get_middle_element(data):
    if not data:
        return None
    index = len(data) // 2
    return data[index]

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [1, 2, 3, 4]
    sample_empty = []

    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))
    print(get_middle_element(sample_empty))