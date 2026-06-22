def get_negated_boolean(values):
    if not isinstance(values, list):
        raise TypeError("Input must be a list")
    if len(values) != 1:
        raise ValueError("List must contain exactly one element")
    element = values[0]
    if not isinstance(element, bool):
        raise TypeError("List element must be a boolean")
    return not element

class BooleanNegator:
    def __init__(self, initial_value):
        self.value = initial_value

    def negate(self):
        self.value = not self.value
        return self.value

if __name__ == '__main__':
    sample_list = [True]
    negated_value = get_negated_boolean(sample_list)
    print(negated_value)
    
    negator = BooleanNegator(False)
    result = negator.negate()
    print(result)