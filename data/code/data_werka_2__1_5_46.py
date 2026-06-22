class InvalidWeightError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativeWeightError(InvalidWeightError):
    def __init__(self, message):
        super().__init__(message)

class WeightTooHighError(InvalidWeightError):
    def __init__(self, message):
        super().__init__(message)

def weight_validator(max_weight=200):
    def decorator(func):
        def wrapper(weight):
            if not isinstance(weight, (int, float)):
                raise TypeError('Weight must be a number.')
            if weight < 0:
                raise NegativeWeightError('Weight cannot be negative.')
            if weight > max_weight:
                raise WeightTooHighError(f'Weight cannot exceed {max_weight} kg.')
            normalized_weight = round(weight, 2)
            return func(normalized_weight)
        return wrapper
    return decorator

@weight_validator(max_weight=300)
def process_weight(weight):
    return f'Processed weight: {weight} kg'

if __name__ == '__main__':
    try:
        print(process_weight(150))
        print(process_weight(-50))
        print(process_weight("100"))
        print(process_weight(400))
    except (TypeError, InvalidWeightError) as e:
        print(e)