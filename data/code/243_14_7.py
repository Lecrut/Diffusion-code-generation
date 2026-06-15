import numpy as np
def analyze_and_optimize(data):
    a = data['a']
    b = data['b']
    c = data['c']
    try:
        result1 = (a**2 + b**2) / c
        result2 = np.sqrt(result1)
        result3 = a * result2 - b
        return result1, result2, result3
    except ZeroDivisionError:
        return None, None, None
    except ValueError:
        return None, None, None
if __name__ == '__main__':
    sample_data = {
        'a': 3,
        'b': 4,
        'c': 5
    }
    result1, result2, result3 = analyze_and_optimize(sample_data)
    if result1 is not None:
        print(f"Result 1: {result1}")
        print(f"Result 2: {result2}")
        print(f"Result 3: {result3}")