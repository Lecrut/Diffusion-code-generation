class InvalidWeightError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativeWeightError(InvalidWeightError):
    def __init__(self, message):
        super().__init__(message)

class WeightTooHighError(InvalidWeightError):
    def __init__(self, message):
        super().__init__(message)

def weight_validator(func):
    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise ValueError('Weight must be a number.')
        if weight < 0:
            raise NegativeWeightError('Weight cannot be negative.')
        if weight > 300:
            raise WeightTooHighError('Weight cannot exceed 300 kg.')
        normalized_weight = round(weight, 2)
        return func(normalized_weight)
    return wrapper

@weight_validator
def process_weight(weight):
    return f'Processed weight: {weight} kg'

if __name__ == '__main__':
    try:
        print(process_weight(150))
        print(process_weight(-50))
        print(process_weight("100"))
        print(process_weight(350))
    except (TypeError, ValueError) as e:
        print(e)