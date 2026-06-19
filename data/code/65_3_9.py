class StringListHandler:

    def __init__(self, strings):
        self.strings = strings

    def get_string_at_position(self, position):
        if position < 0 or position >= len(self.strings):
            raise ValueError('Invalid position')
        return self.strings[position]
if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry', 'date']
    handler = StringListHandler(sample_strings)
    try:
        result1 = handler.get_string_at_position(1)
        print(result1)
    except ValueError as e:
        print(e)
    try:
        result2 = handler.get_string_at_position(3)
        print(result2)
    except ValueError as e:
        print(e)
    try:
        result3 = handler.get_string_at_position(4)
        print(result3)
    except ValueError as e:
        print(e)