def weight_validator(func):
    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be an integer or float.")
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        return func(weight)
    return wrapper

@weight_validator
def process_weight(weight):
    normalized_weight = round(weight, 2)
    return f"Processed Weight: {normalized_weight} kg"

if __name__ == '__main__':
    try:
        print(process_weight(75.346))
        print(process_weight(-10))
        print(process_weight("100"))
    except (TypeError, ValueError) as e:
        print(e)