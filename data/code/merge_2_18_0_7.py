def reverse_sequence(sequence):
    if isinstance(sequence, (list, tuple)):
        return sequence[::-1]
    elif isinstance(sequence, str):
        return sequence[::-1]
    else:
        raise TypeError("Unsupported type for reversal")
if __name__ == '__main__':
    test_list = [1, 2, 3, 'a', 'b']
    test_tuple = (5, 6, 7)
    test_string = "Hello"
    print(f"Original List: {test_list}")
    reversed_list = reverse_sequence(test_list)
    print(f"Reversed List: {reversed_list}, Type: {type(reversed_list)}")
    print(f"\nOriginal Tuple: {test_tuple}")
    try:
        reversed_tuple = reverse_sequence(test_tuple)
        print(f"Reversed Tuple: {reversed_tuple}, Type: {type(reversed_tuple)}")
    except Exception as e:
        print(e)
    print(f"\nOriginal String: '{test_string}'")
    reversed_string = reverse_sequence(test_string)
    print(f"Reversed String: '{reversed_string}', Type: {type(reversed_string)}")