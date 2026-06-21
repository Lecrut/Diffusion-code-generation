def safe_first_element(sequence):
    if len(sequence) == 0:
        raise IndexError("sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    test_sequence = [10, 20, 30]
    empty_sequence = []
    print(safe_first_element(test_sequence))
    try:
        print(safe_first_element(empty_sequence))
    except IndexError as e:
        print(f"Error: {e}")