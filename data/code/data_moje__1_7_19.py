import functools

class InvalidWeightTypeError(TypeError):
    def __init__(self, value):
        message = "Weight must be a number (int or float), not {}.".format(type(value).__name__)
        super().__init__(message)

class ImpossibleWeightValueError(ValueError):
    def __init__(self, value):
        message = "Weight value {} is impossible. It must be between 0.0 and 500.0 kg.".format(value)
        super().__init__(message)

MIN_WEIGHT_LIMIT = 0.0
MAX_WEIGHT_LIMIT = 500.0

def _check_weight_type(value):
    if isinstance(value, bool):
        return False
    if not isinstance(value, (int, float)):
        return False
    return True

def _check_weight_range(value):
    return MIN_WEIGHT_LIMIT < value <= MAX_WEIGHT_LIMIT

def weight_validator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        weight_arg = None
        if args:
            weight_arg = args[0]
        else:
            raise InvalidWeightTypeError("No weight argument provided")

        if not _check_weight_type(weight_arg):
            raise InvalidWeightTypeError(weight_arg)

        if not _check_weight_range(weight_arg):
            raise ImpossibleWeightValueError(weight_arg)

        normalized_weight = float(weight_arg)
        return func(normalized_weight, *args[1:], **kwargs)
    return wrapper

@weight_validator
def calculate_bmi(weight_kg, height_m):
    if height_m <= 0:
        raise ValueError("Height must be positive")
    return weight_kg / (height_m * height_m)

@weight_validator
def get_weight_category(weight_kg):
    if weight_kg < 50:
        return "Underweight"
    elif weight_kg < 80:
        return "Normal"
    elif weight_kw < 120:
        return "Overweight"
    else:
        return "Obese"

if __name__ == '__main__':
    valid_weights = [65, 70.5, 100, 0.1]
    invalid_weights = [-5, 600, "fifty", True, None]

    for w in valid_weights:
        try:
            bmi = calculate_bmi(w, 1.75)
            print("Weight: {} kg -> BMI: {:.2f}".format(w, bmi))
        except Exception as e:
            print("Error for weight {}: {}".format(w, e))

    for w in invalid_weights:
        try:
            result = calculate_bmi(w, 1.75)
            print("Unexpected success for {}: {}".format(w, result))
        except (InvalidWeightTypeError, ImpossibleWeightValueError) as e:
            print("Correctly caught error for {}: {}".format(w, e))

    test_cat_weight = 120
    try:
        cat = get_weight_category(test_cat_weight)
        print("Weight {} category: {}".format(test_cat_weight, cat))
    except Exception as e:
        print("Error calculating category for {}: {}".format(test_cat_weight, e))