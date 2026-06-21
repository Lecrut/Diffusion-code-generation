def evaluate_logic(p, q):
    r = p ^ q
    first_part = p and q
    second_part = (not p) and r
    return first_part or second_part

def main():
    samples = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    results = {}
    for p_val, q_val in samples:
        results[(p_val, q_val)] = evaluate_logic(p_val, q_val)
    print(results)

if __name__ == '__main__':
    main()