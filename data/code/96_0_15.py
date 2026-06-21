TRUE = True
FALSE = False

def evaluate_nested_logic(a, b, c, d):
    ab_result = a and b
    cd_result = c and not d
    return ab_result or cd_result

if __name__ == '__main__':
    val_a = TRUE
    val_b = FALSE
    val_c = TRUE
    val_d = FALSE
    outcome = evaluate_nested_logic(val_a, val_b, val_c, val_d)
    print(outcome)