def calculate_weight_difference(weight1: float, weight2: float) -> float:
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weights = {
        'Alice': 65.3,
        'Bob': 70.8
    }
    difference = calculate_weight_difference(weights['Alice'], weights['Bob'])
    print(difference)