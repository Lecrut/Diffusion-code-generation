class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    try:
        value1 = SortableValue(100)
        value2 = SortableValue(50)
        value3 = SortableValue('string')
        print('Is value1 greater than value2?', value1.is_greater_than(value2.value))
        print('Is value2 greater than value1?', value2.is_greater_than(value1.value))
        try:
            print('Is value1 greater than value3?', value1.is_greater_than(value3.value))
        except ValueError as e:
            print(e)
    except Exception as e:
        print(f'An error occurred: {e}')