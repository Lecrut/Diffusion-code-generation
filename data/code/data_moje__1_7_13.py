def validate_weight(func):
    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")
        if weight <= 0:
            raise ValueError("Weight must be positive")
        if weight > 2000:
            raise ValueError("Weight exceeds reasonable maximum")
        normalized_weight = float(weight)
        return func(normalized_weight)
    return wrapper

@validate_weight
def process_weight(weight):
    return weight * 2.2

if __name__ == '__main__':
    try:
        result1 = process_weight(70)
        print(result1)
    except Exception as e:
        print(e)
    try:
        result2 = process_weight(-5)
        print(result2)
    except Exception as e:
        print(e)
    try:
        result3 = process_weight("hello")
        print(result3)
    except Exception as e:
        print(e)
    try:
        result4 = process_weight(3000)
        print(result4)
    except Exception as e:
        print(e)