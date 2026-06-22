def evaluate_boolean_pair(left: bool, right: bool) -> bool:
    outcomes = {
        (True, True): False,
        (True, False): False,
        (False, True): False,
        (False, False): True
    }
    return outcomes[(left, right)]

if __name__ == '__main__':
    a = True
    b = False
    output = evaluate_boolean_pair(a, b)
    print(output)