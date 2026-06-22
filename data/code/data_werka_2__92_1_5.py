def find_opposite_truth(val: bool) -> bool:
    if val:
        return False
    return True

if __name__ == '__main__':
    true_val = True
    false_val = False
    res_true = find_opposite_truth(true_val)
    res_false = find_opposite_truth(false_val)
    print(res_true)
    print(res_false)