def reverse_iterable(data):
    return list(reversed(list(data))) if not isinstance(data, (str, bytes)) else data[::-1]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    print(f"Original List: {sample_list}")
    reversed_list = reverse_iterable(sample_list)
    print(f"Reversed List: {reversed_list}")
    print(f"\nOriginal Tuple: {sample_tuple}")
    reversed_tuple = tuple(reverse_iterable(sample_tuple))
    print(f"Reversed Tuple: {reversed_tuple}")
    print(f"\nOriginal String: '{sample_string}'")
    reversed_string = reverse_iterable(sample_string)
    print(f"Reversed String: '{reversed_string}'")