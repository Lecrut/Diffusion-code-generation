def find_opposite_truth(truth):
    if truth:
        return False
    return True

if __name__ == '__main__':
    input_val = True
    output_val = find_opposite_truth(input_val)
    print(output_val)
    input_val2 = False
    output_val2 = find_opposite_truth(input_val2)
    print(output_val2)