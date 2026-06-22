def weight_validator(func):

    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError('Weight must be an integer or float.')
        if weight < 0:
            raise ValueError('Weight cannot be negative.')
        return func(weight)
    return wrapper

@weight_validator
def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi
if __name__ == '__main__':
    try:
        print(calculate_bmi(70, 1.75))
        print(calculate_bmi(-70, 1.75))
        print(calculate_bmi('70', 1.75))
    except (TypeError, ValueError) as e:
        print(e)