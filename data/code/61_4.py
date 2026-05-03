def get_string_at_position(string_list, position):
    if position < 0:
        return "Error: Position cannot be negative."
    if position >= len(string_list):
        return "Error: Position out of bounds."
    return string_list[position]
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    position1 = 2
    result1 = get_string_at_position(sample_list, position1)
    print(f"List: {sample_list}")
    print(f"Position: {position1}, Result: {result1}")
    position2 = -1
    result2 = get_string_at_position(sample_list, position2)
    print(f"List: {sample_list}")
    print(f"Position: {position2}, Result: {result2}")
    position3 = 4
    result3 = get_string_at_position(sample_list, position3)
    print(f"List: {sample_list}")
    print(f"Position: {position3}, Result: {result3}")