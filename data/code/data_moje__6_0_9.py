UNIT_MAP = {"default": 1.0}

def calculate_weight_difference(weight1: float, weight2: float) -> float:
    factor = UNIT_MAP["default"]
    diff = weight1 - weight2
    if diff < 0:
        return -diff * factor
    return diff * factor

if __name__ == '__main__':
    val_a = 200.75
    val_b = 198.30
    output = calculate_weight_difference(val_a, val_b)
    print(output)