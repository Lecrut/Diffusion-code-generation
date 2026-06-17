def process_pairs(pairs):
    for pair in pairs:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2 or not all(isinstance(x, (int, float)) for x in pair):
            raise ValueError("All pairs must contain exactly two numbers.")
    averages = []
    for pair in pairs:
        try:
            avg = (pair[0] + pair[1]) / 2
            averages.append(avg)
        except TypeError:
            raise ValueError("Error calculating average for a pair.")
    return averages
if __name__ == '__main__':
    sample_data_valid = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    sample_data_invalid_length = [
        [1, 2],
        [3],
        [5, 6]
    ]
    sample_data_invalid_type = [
        [1, 'a'],
        [3, 4]
    ]
    print("--- Testing Valid Data ---")
    try:
        result_valid = process_pairs(sample_data_valid)
        print(result_valid)
    except ValueError as e:
        print(f"Caught expected error for valid data: {e}")
    print("\n--- Testing Invalid Length Data ---")
    try:
        process_pairs(sample_data_invalid_length)
    except ValueError as e:
        print(f"Successfully caught error for invalid length: {e}")
    print("\n--- Testing Invalid Type Data ---")
    try:
        process_pairs(sample_data_invalid_type)
    except ValueError as e:
        print(f"Successfully caught error for invalid type: {e}")