def compute_boolean_logic(val_a, val_b):
    if not isinstance(val_a, bool) or not isinstance(val_b, bool):
        raise ValueError("Arguments must be boolean types")
    inputs = [val_a, val_b]
    results = {
        "input_1": val_a,
        "input_2": val_b,
        "conjunction": val_a and val_b,
        "disjunction": val_a or val_b,
        "exclusive_or": val_a ^ val_b,
        "negation_1": not val_a,
        "negation_2": not val_b,
        "implication_forward": (not val_a) or val_b,
        "implication_reverse": (not val_b) or val_a,
        "equivalence": val_a == val_b,
        "nand": not (val_a and val_b),
        "nor": not (val_a or val_b)
    }
    return results

if __name__ == '__main__':
    out = compute_boolean_logic(True, False)
    print(out)