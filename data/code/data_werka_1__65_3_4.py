class StringListHandler:
    def __init__(self, strings):
        self.strings = strings

    def get_string_at_position(self, position):
        if not isinstance(position, int):
            raise TypeError("Position must be an integer")
        if position < 0 or position >= len(self.strings):
            raise ValueError("Invalid position")
        return self.strings[position]

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry', 'date']
    handler = StringListHandler(sample_strings)
    try:
        result = handler.get_string_at_position(2)
        print(result)
    except (ValueError, TypeError) as e:
        print(e)