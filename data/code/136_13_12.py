def evaluate_logic(a: bool, b: bool) -> str:
    decisions = {
        (True, False): 'Decision A',
        (False, True): 'Decision B'
    }
    return decisions.get((a, b), 'No Decision')

if __name__ == '__main__':
    print(evaluate_logic(True, False))
    print(evaluate_logic(False, True))
    print(evaluate_logic(True, True))
    print(evaluate_logic(False, False))