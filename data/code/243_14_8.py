import numpy as np
def analyze_and_optimize(data):
    a = data['a']
    b = data['b']
    c = data['c']
    try:
        result1 = (a**2 + b**2) / c
        result2 = np.sqrt(result1)
        result3 = result1 * 2
        return {
            "result1": result1,
            "result2": result2,
            "result3": result3
        }
    except ZeroDivisionError:
        return {"error": "Division by zero encountered"}
    except ValueError:
        return {"error": "Invalid input for square root or other math operation"}
if __name__ == '__main__':
    sample_data = {
        'a': 3,
        'b': 4,
        'c': 5
    }
    results = analyze_and_optimize(sample_data)
    print(results)