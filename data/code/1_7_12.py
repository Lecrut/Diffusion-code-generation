import functools

MAX_KG = 500
MIN_KG = 0.01

class WeightTypeException(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__("Weight must be a numeric type, not {}".format(type(value).__name__))

class WeightRangeException(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__("Weight {} is out of allowed range ({:.2f} to {:.2f} kg)".format(value, MIN_KG, MAX_KG))

def normalize_weight(value):
    if isinstance(value, bool):
        raise WeightTypeException(value)
    if not isinstance(value, (int, float)):
        raise WeightTypeException(value)
    normalized = float(value)
    if normalized <= 0:
        raise WeightRangeException(normalized)
    if normalized > MAX_KG:
        raise WeightRangeException(normalized)
    return normalized

def weight_validator(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if not args:
            raise WeightTypeException("missing weight argument")
        raw_weight = args[0]
        clean_weight = normalize_weight(raw_weight)
        new_args = (clean_weight,) + args[1:]
        return func(*new_args, **kwargs)
    return decorator

@weight_validator
def calculate_shipping_cost(weight):
    rate = 0.05
    base_fee = 5.0
    return base_fee + (weight * rate)

@weight_validator
def log_weight_entry(weight, description):
    return "Logged: {} kg for {}".format(weight, description)

if __name__ == '__main__':
    print(calculate_shipping_cost(150))
    print(calculate_shipping_cost(250.5))
    try:
        calculate_shipping_cost(-10)
    except WeightRangeException as e:
        print(e)
    try:
        calculate_shipping_cost("heavy")
    except WeightTypeException as e:
        print(e)
    try:
        calculate_shipping_cost(True)
    except WeightTypeException as e:
        print(e)
    print(log_weight_entry(12.5, "package_a"))
    print(log_weight_entry(500, "package_b"))
    try:
        log_weight_entry(501, "package_c")
    except WeightRangeException as e:
        print(e)