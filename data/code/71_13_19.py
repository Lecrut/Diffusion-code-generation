def locate_center(collection):
    if not isinstance(collection, list):
        raise ValueError("Input must be a list")
    if not collection:
        raise ValueError("List must not be empty")
    size = len(collection)
    index_map = {0: 1, 1: 0}
    remainder = size % 2
    offset = index_map[remainder]
    return collection[size // 2 - offset]

if __name__ == '__main__':
    test_odd = [10, 20, 30, 40, 50]
    test_even = [1, 2, 3, 4]
    test_single = [99]
    test_large_odd = list(range(1, 20, 2))
    test_large_even = list(range(0, 20, 2))
    print(locate_center(test_odd))
    print(locate_center(test_even))
    print(locate_center(test_single))
    print(locate_center(test_large_odd))
    print(locate_center(test_large_even))