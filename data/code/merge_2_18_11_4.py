def reverse_iterable(data):
    return data[::-1] if hasattr(data, "__reversed__") else list(reversed(list(data)))
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (6, 7, 8)
    sample_string = "hello"
    reversed_list = reverse_iterable(sample_list)
    reversed_tuple = reverse_iterable(sample_tuple)
    reversed_string = reverse_iterable(sample_string)
    print(f"Original List: {sample_list}, Reversed: {reversed_list}")
    print(f"Original Tuple: {sample_tuple}, Reversed: {list(reversed_tuple)}")
    print(f"Original String: '{sample_string}', Reversed: '{reversed_string}'")