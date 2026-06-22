def compute_logic_table(val_a, val_b):
    if type(val_a) is not bool or type(val_b) is not bool:
        raise ValueError("Parameters must be strictly boolean")
    results = {}
    results["val_a"] = val_a
    results["val_b"] = val_b
    results["conjunction"] = val_a and val_b
    results["disjunction"] = val_a or val_b
    results["exclusive_or"] = val_a ^ val_b
    results["negation_a"] = not val_a
    results["negation_b"] = not val_b
    results["implication_a_b"] = (not val_a) or val_b
    results["implication_b_a"] = (not val_b) or val_a
    results["equivalence"] = (val_a == val_b)
    results["nand"] = not (val_a and val_b)
    results["nor"] = not (val_a or val_b)
    return results

if __name__ == '__main__':
    output = compute_logic_table(True, False)
    print(output)