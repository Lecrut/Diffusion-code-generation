def get_middle_element(items):
    count = len(items)
    if count == 0:
        raise ValueError("List must not be empty")
    half = count // 2
    if count % 2 == 1:
        return items[half]
    left = items[half - 1]
    right = items[half]
    return (left + right) / 2.0

if __name__ == '__main__':
    sample = [10, 20, 30, 40, 50]
    odd_result = get_middle_element(sample)
    print(odd_result)
    sample_even = [10, 20, 30, 40]
    even_result = get_middle_element(sample_even)
    print(even_result)