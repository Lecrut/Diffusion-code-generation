class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    values = {'value1': SortableValue(35), 'value2': SortableValue(40), 'value3': SortableValue(25)}
    result = values['value1'].is_greater_than(values['value2'].value)
    print(f'Is value1 greater than value2? {result}')
    result = values['value3'].is_greater_than(values['value1'].value)
    print(f'Is value3 greater than value1? {result}')
    try:
        result = values['value1'].is_greater_than('a string')
    except ValueError as e:
        print(e)