def get_string_at_position(string_list, position):
    if position < 0:
        return "Error: Position cannot be negative."
    if position >= len(string_list):
        return "Error: Position out of bounds."
    return string_list[position]

if __name__ == '__main__':
    sample_list = ["kiwi", "mango", "papaya", "grape"]
    positions_to_check = [2, -1, 3, 5]
    
    for position in positions_to_check:
        result = get_string_at_position(sample_list, position)
        print(f"List: {sample_list}")
        print(f"Position: {position}, Result: {result}")