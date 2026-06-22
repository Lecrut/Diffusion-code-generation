def find_opposite_truth(truth):
    if truth:
        return False
    return True

if __name__ == '__main__':
    true_val = True
    false_val = False
    print(find_opposite_truth(true_val))
    print(find_opposite_truth(false_val))