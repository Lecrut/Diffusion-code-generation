def validate_and_normalize_weight(func):
    def wrapper(weight_value):
        if not isinstance(weight_value, (int, float)):
            raise TypeError(f"Weight must be a number, got {type(weight_value).__name__}")
        if weight_value < 0:
            raise ValueError(f"Weight cannot be negative, got {weight_value}")
        normalized = float(weight_value)
        return func(normalized)
    return wrapper

@validate_and_normalize_weight
def process_weight(weight):
    return weight * 2.2

if __name__ == '__main__':
    try:
        result1 = process_weight(70)
        print(result1)
    except Exception as e:
        print(e)

    try:
        result2 = process_weight(0)
        print(result2)
    except Exception as e:
        print(e)

    try:
        result3 = process_weight(-5)
        print(result3)
    except Exception as e:
        print(e)

    try:
        result4 = process_weight("100")
        print(result4)
    except Exception as e:
        print(e)

    try:
        result5 = process_weight(120.5)
        print(result5)
    except Exception as e:
        print(e)