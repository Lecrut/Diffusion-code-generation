def find_max_element(iterable):
    return max(iterable, key=lambda x: x)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_max_element(sample_values))