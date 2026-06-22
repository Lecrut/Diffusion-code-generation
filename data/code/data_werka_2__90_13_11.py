THRESHOLD = 10
CONDITIONS = {
    'left': lambda v: v > THRESHOLD,
    'right': lambda v: v > THRESHOLD
}

def evaluate_threshold_or(left_val, right_val):
    left_result = CONDITIONS['left'](left_val)
    right_result = CONDITIONS['right'](right_val)
    return left_result or right_result

if __name__ == '__main__':
    val_a = 15
    val_b = 4
    outcome = evaluate_threshold_or(val_a, val_b)
    print(outcome)