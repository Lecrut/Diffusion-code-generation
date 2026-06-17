import math
def calculate_equivalent_weight(formula, atomic_weights):
    elements = {}
    for char in formula:
        if 'A' <= char <= 'Z':
            elements[char] = elements.get(char, 0) + 1
        elif '0' <= char <= '9':
            pass
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
        print(f"{formula}: {equivalent_weight}")
    except ValueError as e:
        print(e)