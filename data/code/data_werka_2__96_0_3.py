def evaluate_nested_logic(a, b, c, d):
    truth_table = {
        (True, True): True,
        (True, False): False,
        (False, True): False,
        (False, False): False,
    }
    ab = truth_table[(a, b)]
    cd = truth_table[(c, not d)]
    return ab or cd

if __name__ == '__main__':
    result = evaluate_nested_logic(True, True, False, True)
    print(result)