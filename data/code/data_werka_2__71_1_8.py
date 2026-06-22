def find_middle_element(data):
    if not data:
        raise ValueError("List must not be empty")
    index = len(data) // 2
    if len(data) % 2 == 0:
        index -= 1
    return data[index]

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [100, 200, 300, 400]
    sample_single = [999]
    print(find_middle_element(sample_odd))
    print(find_middle_element(sample_even))
    print(find_middle_element(sample_single))