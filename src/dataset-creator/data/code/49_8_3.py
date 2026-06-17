import cmath
def is_positive(value):
    try:
        if isinstance(value, (int, float)):
            return value > 0
        elif isinstance(value, complex):
            return value.real > 0
        else:
            raise TypeError(f"Unsupported type {type(value).__name__}")
    except Exception as e:
        print(f"Validation error for input of type {type(e)}")
        return False
if __name__ == '__main__':
    test_cases = [5, -3.2, 0, complex(1, 4), complex(-1, 9)]
    results = []
    for case in test_cases:
        result = is_positive(case)
        results.append((case, result))
    print("Validation Results:")
    for item, res in results:
        if isinstance(item, complex):
            print(f"Complex {item}: {'Positive' if res else 'Not Positive'}")
        else:
            print(f"{type(item).__name__} {item}: {'Positive' if res else 'Not Positive'}")