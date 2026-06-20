import functools

class InvalidWeightType(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidWeightValue(Exception):
    def __init__(self, message):
        super().__init__(message)

VALID_WEIGHT_MIN = 0.0
VALID_WEIGHT_MAX = 500.0

def ensure_numeric(weight):
    if isinstance(weight, bool):
        raise InvalidWeightType("Weight cannot be a boolean")
    if not isinstance(weight, (int, float)):
        raise InvalidWeightType(f"Expected numeric type, got {type(weight).__name__}")
    return float(weight)

def check_range(weight):
    if weight < VALID_WEIGHT_MIN:
        raise InvalidWeightValue(f"Weight {weight} is below minimum {VALID_WEIGHT_MIN}")
    if weight > VALID_WEIGHT_MAX:
        raise InvalidWeightValue(f"Weight {weight} exceeds maximum {VALID_WEIGHT_MAX}")

def weight_validator_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise InvalidWeightType("Missing weight argument")
        raw_weight = args[0]
        validated_weight = ensure_numeric(raw_weight)
        check_range(validated_weight)
        normalized_args = (validated_weight,) + args[1:]
        return func(*normalized_args, **kwargs)
    return wrapper

@weight_validator_decorator
def calculate_bmi(weight, height=1.75):
    return weight / (height * height)

if __name__ == '__main__':
    print(calculate_bmi(70))
    print(calculate_bmi(70.5))
    try:
        calculate_bmi("70")
    except InvalidWeightType as e:
        print(e)
    try:
        calculate_bmi(-5)
    except InvalidWeightValue as e:
        print(e)
    try:
        calculate_bmi(600)
    except InvalidWeightValue as e:
        print(e)
    try:
        calculate_bmi(True)
    except InvalidWeightType as e:
        print(e)