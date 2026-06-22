def find_middle_element(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    if len(data) == 0:
        raise ValueError("List must not be empty")
    index = (len(data) - 1) // 2
    return data[index]

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [10, 20, 30, 40]
    print(find_middle_element(sample_odd))
    print(find_middle_element(sample_even))