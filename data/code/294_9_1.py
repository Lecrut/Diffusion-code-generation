def calculate_equivalent_weight(formula, atomic_weights):
    elements = {}
    for symbol in formula:
        elements[symbol] = elements.get(symbol, 0) + 1
    total_weight = 0
    for element, count in elements.items():
        if element in atomic_weights:
            total_weight += count * atomic_weights[element]
        else:
            raise ValueError(f"Atomic weight for {element} not found")
    return total_weight
if __name__ == '__main__':
    formula = "H2O"
    atomic_weights = {
        "H": 1.008,
        "O": 15.999
    }
    try:
        equivalent_weight = calculate_equivalent_weight(formula, atomic_weights)
        print(f"Formula: {formula}")
        print(f"Equivalent Weight: {equivalent_weight:.3f}")
    except ValueError as e:
        print(f"Error: {e}")
    formula2 = "CO2"
    atomic_weights2 = {
        "C": 12.011,
        "O": 15.999
    }
    try:
        equivalent_weight2 = calculate_equivalent_weight(formula2, atomic_weights2)
        print(f"\nFormula: {formula2}")
        print(f"Equivalent Weight: {equivalent_weight2:.3f}")
    except ValueError as e:
        print(f"Error: {e}")