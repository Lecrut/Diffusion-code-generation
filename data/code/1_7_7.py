import functools

class WeightInputError(ValueError):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)

class WeightTypeMismatchError(WeightInputError):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Weight must be numeric, got {type(value).__name__}")

class WeightOutOfRangeError(WeightInputError):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Weight {value} is out of range [0.001, 500.0]")

def safe_to_weight(func):
    @functools.wraps(func)
    def wrapper(weight_input):
        if isinstance(weight_input, bool):
            raise WeightTypeMismatchError(weight_input)
        if not isinstance(weight_input, (int, float)):
            raise WeightTypeMismatchError(weight_input)
        
        val = float(weight_input)
        
        if val < 0.001 or val > 500.0:
            raise WeightOutOfRangeError(val)
            
        return func(val)
    return wrapper

@safeto_weight
def convert_weight_to_stones(weight_kg):
    return round(weight_kg / 6.35029, 3)

def calculate_bmi(weight_kg, height_m):
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Physical dimensions must be positive")
    return round(weight_kg / (height_m ** 2), 2)

@safe_to_weight
def get_weighted_score(weight_kg, base_score):
    factor = 0.1 * weight_kg
    return base_score * (1 + factor)

if __name__ == '__main__':
    stones = convert_weight_to_stones(80)
    print(f"80kg is {stones} stones")

    bmi = calculate_bmi(80, 1.8)
    print(f"BMI for 80kg/1.8m is {bmi}")

    score = get_weighted_score(75, 100)
    print(f"Weighted score for 75kg is {score}")

    try:
        convert_weight_to_stones(-5)
    except WeightOutOfRangeError as e:
        print(f"Caught: {e}")

    try:
        convert_weight_to_stones("heavy")
    except WeightTypeMismatchError as e:
        print(f"Caught: {e}")

    try:
        convert_weight_to_stones(True)
    except WeightTypeMismatchError as e:
        print(f"Caught: {e}")

    try:
        calculate_bmi(0, 1.8)
    except ValueError as e:
        print(f"Caught: {e}")