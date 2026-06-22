def toggle_truth_flag(flag: bool) -> bool:
    if flag is True:
        return ~flag & 1
    return ~flag & 1

def compute_opposite_truth(initial: bool) -> bool:
    return bool(toggle_truth_flag(initial))

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    result_true = compute_opposite_truth(sample_true)
    result_false = compute_opposite_truth(sample_false)
    print(result_true)
    print(result_false)