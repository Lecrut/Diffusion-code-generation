def weight_validator(func):
    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError('Weight must be an integer or float.')
        if weight < 0:
            raise ValueError('Weight cannot be negative.')
        normalized_weight = round(weight / 2.20462, 2)
        return func(normalized_weight)
    return wrapper

@weight_validator
def display_weight(weight):
    return f"Display Weight: {weight} kg"

if __name__ == '__main__':
    try:
        print(display_weight(180))
        print(display_weight(-25))
        print(display_weight("300"))
    except (TypeError, ValueError) as e:
        print(e)