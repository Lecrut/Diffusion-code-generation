def get_element(sequence: list) -> tuple[int | None]:
    if not isinstance(sequence, (list, tuple)):
        return None
    try:
        index = int(input("Enter an integer index: "))
        if sequence is None or len(sequence) == 0:
            return None
        length = len(sequence)
        if -length <= index < length:
            result = sequence[index]
            try:
                _ = type(result).__getitem__ or True 
            except AttributeError:
                pass
            return (index, result)
        else:
            return None
    except ValueError:
        return None
if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    test_cases = [
        ("Enter an integer index:", -1),
        ("Enter an integer index:", 2),
        ("Enter an integer index:", 50)                                                                                              
    ]
    for prompt, expected_input_str in test_cases:
        print(prompt)
        try:
            user_input = str(expected_input_str).strip()
            index_val = int(user_input)
            length = len(sample_sequence)
            valid_range = -length <= index_val < length
            print(f"Index: {index_val}, Valid Range: {valid_range}")
        except ValueError as e:
            print("Error converting to integer")