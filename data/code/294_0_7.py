def calculate_equivalent_weight(weights, molar_weights):
    return sum(weight * mw for weight, mw in zip(weights, molar_weights))

if __name__ == '__main__':
    weights = [10.0, 5.0]
    molar_weights = [44.0, 18.0]
    result = calculate_equivalent_weight(weights, molar_weights)
    print(result)