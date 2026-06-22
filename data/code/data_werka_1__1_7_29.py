def validate_and_normalize_weight(func):
    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        normalized_weight = round(weight, 2)
        return func(normalized_weight)
    return wrapper

@validate_and_normalize_weight
def print_weight(weight):
    return f"Normalized Weight: {weight} kg"

if __name__ == '__main__':
    try:
        print(print_weight(75.346))
        print(print_weight(-10))
        print(print_weight("100"))
    except (TypeError, ValueError) as e:
        print(e)