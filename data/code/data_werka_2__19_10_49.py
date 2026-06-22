def is_positive(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    return number > 0

class NumberChecker:
    def __init__(self, value):
        self.value = value
    
    def check_positive(self):
        return is_positive(self.value)

if __name__ == '__main__':
    try:
        sample_values = [15, -8, 0, 2, -3]
        results = {value: NumberChecker(value).check_positive() for value in sample_values}
        print(results)
    except ValueError as e:
        print(e)