def validate_weights(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")

def simple_weight_difference(x, y):
    validate_weights(x, y)
    return abs(x - y)

if __name__ == '__main__':
    weight1 = 80
    weight2 = 75
    print(simple_weight_difference(weight1, weight2))