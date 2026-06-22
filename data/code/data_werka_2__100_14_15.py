def evaluate_logic(p, q):
    xor_result = p ^ q
    and_term = p and q
    not_p = not p
    second_term = not_p and xor_result
    return and_term or second_term

def run_tests():
    cases = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    outputs = {}
    for p, q in cases:
        outputs[(p, q)] = evaluate_logic(p, q)
    return outputs

if __name__ == '__main__':
    final_output = run_tests()
    print(final_output)