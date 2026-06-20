import functools

class WeightDataTypeError(TypeError):
    def __init__(self, value):
        self.value = value
        message = "Weight must be a numeric type, not {}.".format(type(value).__name__)
        super().__init__(message)

class WeightValueError(ValueError):
    def __init__(self, value, min_val, max_val):
        self.value = value
        self.min_val = min_val
        self.max_val = max_val
        message = "Weight value {} is out of range [{}, {}].".format(value, min_val, max_val)
        super().__init__(message)

MIN_WEIGHT = 0.0
MAX_WEIGHT = 1000.0

def _normalize_weight(value):
    if isinstance(value, bool):
        raise WeightDataTypeError(value)
    if not isinstance(value, (int, float)):
        raise WeightDataTypeError(value)
    normalized = float(value)
    if normalized < MIN_WEIGHT or normalized > MAX_WEIGHT:
        raise WeightValueError(normalized, MIN_WEIGHT, MAX_WEIGHT)
    return normalized

def weight_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise WeightDataTypeError(None)
        weight_arg = args[0]
        validated_weight = _normalize_weight(weight_arg)
        new_args = (validated_weight,) + args[1:]
        return func(*new_args, **kwargs)
    return wrapper

@weight_decorator
def calculate_dosage(weight_kg):
    base_dose = 5.0
    dosage = base_dose * weight_kg * 1.1
    return round(dosage, 2)

@weight_decorator
def get_health_score(weight_kg):
    if weight_kg < 20:
        return "Underweight Risk"
    elif weight_kg > 150:
        return "Obesity Risk"
    return "Healthy Range"

if __name__ == '__main__':
    print(calculate_dosage(70))
    print(get_health_score(70))
    try:
        calculate_dosage(-5)
    except WeightValueError as e:
        print(e)
    try:
        get_health_score("heavy")
    except WeightDataTypeError as e:
        print(e)