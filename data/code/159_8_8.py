def filter_odd_numbers(data):
    odd_numbers = []
    for item in data:
        if isinstance(item, int) and item % 2 != 0:
            odd_numbers.append(item)
    return odd_numbers

if __name__ == '__main__':
    sample_data = [1, 'a', 3, None, 5, {}, 7, [], 9]
    result = filter_odd_numbers(sample_data)
    print(result)