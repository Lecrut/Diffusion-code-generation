class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    sample_values = {'value1': 45, 'value2': 30, 'value3': 60}
    value1 = SortableValue(sample_values['value1'])
    value2 = SortableValue(sample_values['value2'])
    result1 = value1.is_greater_than(value2.value)
    print(f'Is {value1.value} greater than {value2.value}? {result1}')
    try:
        result2 = value1.is_greater_than('a string')
        print(result2)
    except ValueError as e:
        print(e)
    value3 = SortableValue(sample_values['value3'])
    result3 = value3.is_greater_than(value1.value)
    print(f'Is {value3.value} greater than {value1.value}? {result3}')