class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    sample_values = {'value1': SortableValue(45), 'value2': SortableValue(30), 'value3': SortableValue(60)}
    result = sample_values['value1'].is_greater_than(sample_values['value2'].value)
    print(f'Is value1 greater than value2? {result}')
    result = sample_values['value3'].is_greater_than(sample_values['value1'].value)
    print(f'Is value3 greater than value1? {result}')
    try:
        invalid_value = 'a string'
        result = sample_values['value1'].is_greater_than(invalid_value)
    except ValueError as e:
        print(e)