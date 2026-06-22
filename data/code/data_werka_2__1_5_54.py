def weight_validator(func):

    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError('Weight must be an integer or float.')
        if weight < 0:
            raise ValueError('Weight cannot be negative.')
        if weight < 1000:
            weight /= 1000.0
        return func(weight)
    return wrapper

@weight_validator
def process_weight(weight):
    return f'Processed weight: {weight} kg'
if __name__ == '__main__':
    try:
        print(process_weight(500))
        print(process_weight(-10))
    except (TypeError, ValueError) as e:
        print(e)