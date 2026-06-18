import math
def is_positive_with_precision(value: float) -> bool:
    if value > 1e-9 or value < -1e-9:
        return True
    elif abs(value) <= 1e-9 and not (math.isinf(value) or math.isnan(value)):
        return False
    else:
        return value > 0
if __name__ == '__main__':
    test_cases = [
        float('inf'),
        -float('inf'),
        1.7e308,
        -1.7e308,
        4.9e-324,
        -4.9e-324,
        5.0e-324,
        float('-nan') if False else None,                                                       
    ]
    results = []
    for val in test_cases:
        try:
            res = is_positive_with_precision(val)
            results.append((val, res))
        except Exception as e:
            results.append((f"Error: {e}", False))
    print("Evaluation Results:")
    for item in results:
        if isinstance(item[0], float):
            val_str = f"{item[0]:.15E}" if math.isinf(item[0]) or math.isnan(item[0]) else str(item[0])
            print(f"Value ({val_str}): {'Positive' if item[1] and not (math.isnan(item[0])) else 'Not Positive'}")
        else:
            print(f"{item[0]}: {item[1]}")