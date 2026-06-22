import functools

class WeightTypeException(Exception):
    def __init__(self, value):
        self.value = value
        message = f"Weight must be a number (int or float), not {type(value).__name__}"
        super().__init__(message)

class WeightRangeException(Exception):
    def __init__(self, value):
        self.value = value
        message = f"Weight {value} is out of allowable range [0.0, 1000.0]"
        super().__init__(message)

MIN_WEIGHT_LIMIT = 0.0
MAX_WEIGHT_LIMIT = 1000.0

def normalize_weight_value(value):
    if value is None:
        raise WeightTypeException(value)
    if isinstance(value, bool):
        raise WeightTypeException(value)
    if not isinstance(value, (int, float)):
        raise WeightTypeException(value)
    
    normalized = float(value)
    
    if normalized < MIN_WEIGHT_LIMIT or normalized > MAX_WEIGHT_LIMIT:
        raise WeightRangeException(normalized)
    
    return normalized

def weight_validating_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        weight_arg = None
        if len(args) > 0:
            weight_arg = args[0]
            new_args = (normalize_weight_value(weight_arg),) + args[1:]
            return func(*new_args, **kwargs)
        elif 'weight' in kwargs:
            weight_arg = kwargs['weight']
            kwargs['weight'] = normalize_weight_value(weight_arg)
            return func(*args, **kwargs)
        else:
            raise WeightTypeException(None)
    return wrapper

@weight_validating_decorator
def calculate_bmi(weight_kg, height_m):
    height_m_normalized = float(height_m)
    if height_m_normalized <= 0:
        raise ValueError("Height must be positive")
    return weight_kg / (height_m_normalized ** 2)

def process_mass(weight_input):
    normalized = normalize_weight_value(weight_input)
    return normalized * 2.0

if __name__ == '__main__':
    sample_weights = [80, 0.0, 999, -5, "abc", True, 1500]
    
    print("--- Testing BMI Calculation ---")
    try:
        result = calculate_bmi(70, 1.75)
        print(f"Valid BMI for 70kg: {result}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    try:
        result = calculate_bmi(-10, 1.8)
        print(f"Invalid BMI result: {result}")
    except WeightRangeException as e:
        print(f"Caught range error: {e}")
        
    print("\n--- Testing Mass Processing ---")
    for w in sample_weights:
        try:
            final_value = process_mass(w)
            print(f"Input: {w} -> Processed: {final_value}")
        except WeightTypeException as e:
            print(f"Input: {w} -> Type Error: {e}")
        except WeightRangeException as e:
            print(f"Input: {w} -> Range Error: {e}")