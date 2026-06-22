class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    sample_value1 = 75
    sample_value2 = 30
    sample_value3 = 'hello'
    value_a = SortableValue(sample_value1)
    value_b = SortableValue(sample_value2)
    result1 = value_a.is_greater_than(value_b.value)
    print(f'Is {value_a.value} greater than {value_b.value}? {result1}')
    try:
        result2 = value_a.is_greater_than(sample_value3)
        print(result2)
    except ValueError as e:
        print(e)