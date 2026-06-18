def get_element(sequence: list) -> int | None:
    if not isinstance(sequence, (list, tuple)):
        return None
    try:
        index = int(input("Enter an integer index: "))
        if sequence and -len(sequence) <= index < len(sequence):
            return sequence[index]
        else:
            raise IndexError(f"Index {index} is out of range for length {len(sequence)}")
    except ValueError:
        print("Error: Input must be an integer.")
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    test_cases = [1, -2, 0]
    print("Testing get_element with sample list:", sample_list)
    for idx in test_cases:
        if isinstance(idx, int):
            try:
                result = sample_list[idx]
                print(f"Index {idx}: {result}")
            except IndexError as e:
                print(f"Error at index {idx}: {e}")
        else:
            print(f"Skipping non-integer input type for testing.")