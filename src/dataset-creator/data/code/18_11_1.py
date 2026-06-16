def reverse_iterable(iterable):
    return list(reversed(list(iterable))) if isinstance(iterable, (list, tuple)) else ''.join(reversed(iterable))
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    print("Reversed List:", reverse_iterable(sample_list))
    print("Original List:", sample_list)
    reversed_tuple = reverse_iterable(sample_tuple)
    print("Reversed Tuple:", reversed_tuple)
    print("Original Tuple:", sample_tuple)
    reversed_string = reverse_iterable(sample_string)
    print("Reversed String:", reversed_string)
    print("Original String:", sample_string)