def get_last_element(lst):
    if not lst:
        raise IndexError("Cannot get last element from an empty list")
    reverse_iterator = reversed(lst)
    return next(reverse_iterator)

if __name__ == '__main__':
    test_values = ["red", "green", "blue", "yellow", "purple"]
    final_value = get_last_element(test_values)
    print(final_value)