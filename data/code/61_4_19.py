class StringListHandler:
    ERROR_NEGATIVE_POSITION = "Error: Position cannot be negative."
    ERROR_OUT_OF_BOUNDS = "Error: Position out of bounds."

    @staticmethod
    def get_string_at_position(string_list, position):
        if position < 0:
            return StringListHandler.ERROR_NEGATIVE_POSITION
        if position >= len(string_list):
            return StringListHandler.ERROR_OUT_OF_BOUNDS
        return string_list[position]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    positions_to_check = [2, -1, 4]
    
    for position in positions_to_check:
        result = StringListHandler.get_string_at_position(sample_list, position)
        print(f"List: {sample_list}, Position: {position}, Result: {result}")