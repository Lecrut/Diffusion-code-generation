def boolean_logic_matrix(a, b):
    if type(a) is not bool or type(b) is not bool:
        raise ValueError("Both arguments must be strictly boolean types")
    conjunction = a and b
    disjunction = a or b
    exclusive_or = (a or b) and not (a and b)
    negation_a = not a
    negation_b = not b
    implication_ab = (not a) or b
    implication_ba = (not b) or a
    equality = a == b
    non_implication = (not a) and b
    return {
        "inputs": {
            "var_a": a,
            "var_b": b
        },
        "unary": {
            "not_a": negation_a,
            "not_b": negation_b
        },
        "binary": {
            "a_and_b": conjunction,
            "a_or_b": disjunction,
            "a_xor_b": exclusive_or,
            "a_eq_b": equality,
            "a_implies_b": implication_ab,
            "b_implies_a": implication_ba,
            "a_non_imp_b": non_implication,
            "a_nand_b": not conjunction,
            "a_nor_b": not disjunction
        }
    }

if __name__ == '__main__':
    sample_out = boolean_logic_matrix(True, False)
    print(sample_out)