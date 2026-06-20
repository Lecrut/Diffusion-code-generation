def evaluate_logic(a: bool, b: bool) -> str:
    logic_map = {
        (True, False): 'Decision A',
        (False, True): 'Decision B'
    }
    return logic_map.get((a, b), 'No Decision')

if __name__ == '__main__':
    print(evaluate_logic(True, False))
    print(evaluate_logic(False, True))
    print(evaluate_logic(True, True))
    print(evaluate_logic(False, False))