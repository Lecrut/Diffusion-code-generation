def weight_validator(func):

    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError('Weight must be an integer or float.')
        if weight < 0:
            raise ValueError('Weight cannot be negative.')
        return func(weight)
    return wrapper

@weight_validator
def normalize_weight(weight):
    return round(weight / 2.20462, 2)
if __name__ == '__main__':
    try:
        print(normalize_weight(150))
        print(normalize_weight(-50))
    except (TypeError, ValueError) as e:
        print(e)