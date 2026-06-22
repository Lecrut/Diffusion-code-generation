def evaluate_logic(p, q):
    if not isinstance(p, bool) or not isinstance(q, bool):
        raise ValueError("Inputs must be boolean")
    r = p ^ q
    part1 = p and q
    part2 = (not p) and r
    return part1 or part2

if __name__ == '__main__':
    samples = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    output = {}
    for p_val, q_val in samples:
        key = (p_val, q_val)
        val = evaluate_logic(p_val, q_val)
        output[key] = val
    print(output)