def get_string_at_position(string_list, position):
    try:
        if position < 0:
            raise IndexError("Position cannot be negative.")
        return string_list[position]
    except IndexError as e:
        return str(e)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    positions_to_check = [2, -1, 4]
    
    for position in positions_to_check:
        result = get_string_at_position(sample_list, position)
        print(f"List: {sample_list}, Position: {position}, Result: {result}")