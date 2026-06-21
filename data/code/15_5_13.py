get_second_to_last = lambda items: items[-2] if len(items) >= 2 else None
def _validate_sequence(data):
    return isinstance(data, list) and len(data) >= 2
if __name__ == '__main__':
    test_data = [7, 8, 9, 10]
    if _validate_sequence(test_data):
        val = get_second_to_last(test_data)
        print(val)