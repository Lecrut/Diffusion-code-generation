def find_middle_element(data):
    if not data:
        raise ValueError("List must not be empty")
    length = len(data)
    start = (length - 1) // 2
    end = start + 2 if length % 2 == 0 else start + 1
    middle_slice = data[start:end]
    if length % 2 == 1:
        return middle_slice[0]
    return (middle_slice[0] + middle_slice[1]) / 2

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [10, 20, 30, 40]
    sample_single = [42]
    print(find_middle_element(sample_odd))
    print(find_middle_element(sample_even))
    print(find_middle_element(sample_single))