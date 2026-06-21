KILOS_TO_POUNDS = 2.20462

class InvalidWeightError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativeWeightError(InvalidWeightError):
    def __init__(self, message):
        super().__init__(message)

def validate_weight(weight):
    if not isinstance(weight, (int, float)):
        raise TypeError('Weight must be a number.')
    if weight < 0:
        raise NegativeWeightError('Weight cannot be negative.')

def normalize_weight_decorator(func):
    def wrapper(weight):
        validate_weight(weight)
        normalized_weight = round(weight / KILOS_TO_POUNDS, 2)
        return func(normalized_weight)
    return wrapper

@normalize_weight_decorator
def display_normalized_weight(weight_kg):
    return f'Normalized Weight: {weight_kg} lbs'

if __name__ == '__main__':
    try:
        print(display_normalized_weight(150))
        print(display_normalized_weight(-50))
        print(display_normalized_weight("100"))
    except (TypeError, InvalidWeightError) as e:
        print(e)