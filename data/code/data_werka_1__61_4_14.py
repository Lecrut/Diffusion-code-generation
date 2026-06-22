def get_string_at_position(string_list, position):
    if position < 0:
        return "Error: Position cannot be negative."
    if position >= len(string_list):
        return "Error: Position out of bounds."
    return string_list[position]

if __name__ == '__main__':
    sample_strings = ["dog", "cat", "elephant", "giraffe"]
    test_positions = [2, -1, 3, 4]
    
    for pos in test_positions:
        result = get_string_at_position(sample_strings, pos)
        print(f"List: {sample_strings}")
        print(f"Position: {pos}, Result: {result}")