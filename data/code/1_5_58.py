def weight_validator(func):
    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be an integer or float.")
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        return func(weight)
    return wrapper

@weight_validator
def normalize_weight(weight):
    return round(weight / 2.20462, 2)

if __name__ == '__main__':
    sample_weights = [150, '180', -50, 70.5]
    for weight in sample_weights:
        try:
            normalized = normalize_weight(weight)
            print(f"Normalized Weight: {normalized}")
        except (TypeError, ValueError) as e:
            print(e)