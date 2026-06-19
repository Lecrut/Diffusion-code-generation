def get_string_at_position(string_list, position):
    ERROR_NEGATIVE_POSITION = "Error: Position cannot be negative."
    ERROR_OUT_OF_BOUNDS = "Error: Position out of bounds."

    if position < 0:
        return ERROR_NEGATIVE_POSITION
    if position >= len(string_list):
        return ERROR_OUT_OF_BOUNDS
    return string_list[position]

if __name__ == '__main__':
    SAMPLE_LIST = ["apple", "banana", "cherry", "date"]
    TEST_POSITIONS = [2, -1, 4]

    for pos in TEST_POSITIONS:
        result = get_string_at_position(SAMPLE_LIST, pos)
        print(f"List: {SAMPLE_LIST}")
        print(f"Position: {pos}, Result: {result}")