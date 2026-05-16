def generate_truth_table(a, b):
    results = []
    if a:
        if b:
            results.append((True, True))
        else:
            results.append((True, False))
    else:
        if b:
            results.append((False, True))
        else:
            results.append((False, False))
    return {
        (True, True): (a, b),
        (True, False): (a, b),
        (False, True): (a, b),
        (False, False): (a, b)
    }
if __name__ == '__main__':
    a_val = True
    b_val = False
    truth_table = generate_truth_table(a_val, b_val)
    print(truth_table)