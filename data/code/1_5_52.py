class WeightValidator:
    def __init__(self, func):
        self.func = func

    def validate(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError('Weight must be an integer or float.')
        if weight < 0:
            raise ValueError('Weight cannot be negative.')
        return self.func(weight)

def normalize_weight(weight):
    return round(weight / 2.20462, 2)

if __name__ == '__main__':
    validator = WeightValidator(normalize_weight)
    try:
        print(validator.validate(150))
        print(validator.validate(-50))
        print(validator.validate("100"))
    except (TypeError, ValueError) as e:
        print(e)