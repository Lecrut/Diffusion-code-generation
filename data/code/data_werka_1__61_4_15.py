class StringListAccessor:
    def __init__(self, string_list):
        self.string_list = string_list

    def get_string_at_position(self, position):
        if position < 0:
            return "Error: Position cannot be negative."
        if position >= len(self.string_list):
            return "Error: Position out of bounds."
        return self.string_list[position]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    accessor = StringListAccessor(sample_list)
    
    position1 = 2
    result1 = accessor.get_string_at_position(position1)
    print(f"List: {sample_list}")
    print(f"Position: {position1}, Result: {result1}")
    
    position2 = -1
    result2 = accessor.get_string_at_position(position2)
    print(f"List: {sample_list}")
    print(f"Position: {position2}, Result: {result2}")
    
    position3 = 4
    result3 = accessor.get_string_at_position(position3)
    print(f"List: {sample_list}")
    print(f"Position: {position3}, Result: {result3}")