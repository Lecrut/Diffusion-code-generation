class StringListAccessor:

    def __init__(self, string_list):
        self.string_list = string_list

    def get_string_at_position(self, position):
        if position < 0:
            return 'Error: Position cannot be negative.'
        if position >= len(self.string_list):
            return 'Error: Position out of bounds.'
        return self.string_list[position]
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    accessor = StringListAccessor(sample_list)
    print(accessor.get_string_at_position(0))
    print(accessor.get_string_at_position(2))
    print(accessor.get_string_at_position(-1))
    print(accessor.get_string_at_position(4))