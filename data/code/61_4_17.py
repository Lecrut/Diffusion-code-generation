def get_string_at_position(string_list, position):
    error_messages = {
        "negative_position": "Error: Position cannot be negative.",
        "out_of_bounds": "Error: Position out of bounds."
    }
    
    if position < 0:
        return error_messages["negative_position"]
    if position >= len(string_list):
        return error_messages["out_of_bounds"]
    return string_list[position]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    test_positions = [2, -1, 4]
    
    for pos in test_positions:
        result = get_string_at_position(sample_list, pos)
        print(f"List: {sample_list}, Position: {pos}, Result: {result}")