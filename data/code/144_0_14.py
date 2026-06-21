def compute_truth_table():
    A = True
    B = False
    C = True

    result = (A and B) or not C
    return result

if __name__ == '__main__':
    print(compute_truth_table())