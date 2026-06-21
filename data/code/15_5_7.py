validate_min_length = lambda n, items: items if len(items) >= n else None
get_second_to_last = lambda lst: validate_min_length(2, lst)[-2]
if __name__ == '__main__':
    test_data = [15, 27, 39, 48, 52, 63]
    print(get_second_to_last(test_data))