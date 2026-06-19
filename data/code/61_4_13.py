def get_string_at_position(string_list, position):
    ERROR_MESSAGE = "Error: Position cannot be negative."
    
    if position < 0:
        return ERROR_MESSAGE
    
    if position >= len(string_list):
        return "Error: Position out of bounds."
    
    return string_list[position]

if __name__ == '__main__':
    SAMPLE_LIST = ["apple", "banana", "cherry", "date"]
    POSITIONS_TO_TEST = [2, -1, 4]
    
    for position in POSITIONS_TO_TEST:
        result = get_string_at_position(SAMPLE_LIST, position)
        print(f"List: {SAMPLE_LIST}")
        print(f"Position: {position}, Result: {result}")