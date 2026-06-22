def find_opposite_truth(truth):
    if truth:
        return False
    return True

if __name__ == '__main__':
    val_in = True
    val_out = find_opposite_truth(val_in)
    print(val_out)
    val_in_2 = False
    val_out_2 = find_opposite_truth(val_in_2)
    print(val_out_2)