def is_both_false(a: bool, b: bool) -> bool:
    return a is False and b is False

def evaluate_state(a: bool, b: bool) -> str:
    states = {
        (False, False): "both_false",
        (False, True): "a_false_b_true",
        (True, False): "a_true_b_false",
        (True, True): "both_true"
    }
    return states[(a, b)]

if __name__ == '__main__':
    val_a = False
    val_b = False
    print(is_both_false(val_a, val_b))
    print(evaluate_state(val_a, val_b))