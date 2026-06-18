def reverse_iterable(data):
    return list(reversed(list(data))) if isinstance(data, (str, bytes)) else reversed(data)
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = ('a', 'b')
    sample_string = "hello"
    print(f"Original List: {sample_list}")
    print("Reversed List:", reverse_iterable(sample_list))
    original_copy = list(sample_tuple)
    print(f"\nOriginal Tuple (immutable): {original_copy}")
    reversed_tuple_result = reverse_iterable(sample_tuple)
    print("Reversed Tuple Result:", tuple(reversed(tuple(original_copy))))
    original_str = sample_string
    print(f"\nOriginal String: '{original_str}'")
    reversed_str_result = reverse_iterable(sample_string)
    print("Reversed String Result:", repr(reversed_str_result))