def get_string_at_position(string_list, position):
    if position < 0:
        return "Error: Position cannot be negative."
    if position >= len(string_list):
        return "Error: Position out of bounds."
    return string_list[position]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    test_positions = [2, -1, 4]
    for pos in test_positions:
        result = get_string_at_position(sample_list, pos)
        print(f"List: {sample_list}, Position: {pos}, Result: {result}")