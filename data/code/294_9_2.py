def calculate_equivalent_weight(formula, atomic_weights):
    weights = {}
    for element in formula:
        count = formula.count(element)
        if count > 0:
            weights[element] = weights.get(element, 0) + count * atomic_weights.get(element, 0)
    return weights
if __name__ == '__main__':
    formula = "H2O"
    atomic_weights = {
        "H": 1.008,
        "O": 15.999
    }
    equivalent_weights = calculate_equivalent_weight(formula, atomic_weights)
    print(equivalent_weights)