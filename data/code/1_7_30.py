class InvalidWeightError(Exception):

    def __init__(self, message):
        super().__init__(message)

class NegativeWeightError(InvalidWeightError):

    def __init__(self, message):
        super().__init__(message)

class WeightTooHighError(InvalidWeightError):

    def __init__(self, message):
        super().__init__(message)

def validate_and_normalize_weight(func):

    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise InvalidWeightError('Weight must be a number.')
        if weight < 0:
            raise NegativeWeightError('Weight cannot be negative.')
        if weight > 300:
            raise WeightTooHighError('Weight cannot exceed 300 kg.')
        return func(weight)
    return wrapper

@validate_and_normalize_weight
def process_weight(weight):
    return f'Processed weight: {weight} kg'
if __name__ == '__main__':
    try:
        print(process_weight(150))
        print(process_weight(-5))
    except InvalidWeightError as e:
        print(e)
    try:
        print(process_weight(350))
    except InvalidWeightError as e:
        print(e)
    try:
        print(process_weight('100'))
    except InvalidWeightError as e:
        print(e)