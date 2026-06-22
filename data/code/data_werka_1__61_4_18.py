def get_string_at_position(string_list, position):
    try:
        if position < 0:
            raise ValueError("Position cannot be negative.")
        return string_list[position]
    except IndexError:
        return "Error: Position out of bounds."

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    test_positions = [2, -1, 4]

    for position in test_positions:
        result = get_string_at_position(sample_list, position)
        print(f"List: {sample_list}")
        print(f"Position: {position}, Result: {result}")