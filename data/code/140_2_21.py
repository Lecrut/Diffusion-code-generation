def is_sorted_ascending(numbers):
    return all(x < y for x, y in zip(numbers, numbers[1:]))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(is_sorted_ascending(sample_list))