def evaluate_conditions(a, b, c, d):
    conditions = {
        'cond_a': a > 0,
        'cond_b': b < 10,
        'cond_c': c == 5,
        'cond_d': d is not None
    }
    result = conditions['cond_a'] and conditions['cond_b'] and conditions['cond_c'] and conditions['cond_d']
    return bool(result)

if __name__ == '__main__':
    val_a = 10
    val_b = 5
    val_c = 5
    val_d = "exists"
    output = evaluate_conditions(val_a, val_b, val_c, val_d)
    print(output)