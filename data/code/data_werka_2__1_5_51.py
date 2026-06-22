def weight_validator(func):
    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError('Weight must be an integer or float.')
        if weight < 0:
            raise ValueError('Weight cannot be negative.')
        normalized_weight = round(weight, 2)
        return func(normalized_weight)
    return wrapper

@weight_validator
def convert_to_kg(weight):
    return f"{weight} kg"

if __name__ == '__main__':
    try:
        print(convert_to_kg(160.345))
        print(convert_to_kg(-20))
        print(convert_to_kg("80"))
    except (TypeError, ValueError) as e:
        print(e)