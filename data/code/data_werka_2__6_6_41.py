def calculate_weight_difference(weight1: float, weight2: float) -> float:
    def absolute_value(x: float) -> float:
        return x if x >= 0 else -x
    
    return absolute_value(weight1 - weight2)

if __name__ == '__main__':
    weights = {
        'Alice': 65.3,
        'Bob': 70.8
    }
    difference = calculate_weight_difference(weights['Alice'], weights['Bob'])
    print(difference)