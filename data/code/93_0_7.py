def evaluate_false_pair(first: bool, second: bool) -> bool:
    state_map = {
        (True, True): False,
        (True, False): False,
        (False, True): False,
        (False, False): True,
    }
    return state_map[(first, second)]

if __name__ == '__main__':
    val_a = False
    val_b = False
    outcome = evaluate_false_pair(val_a, val_b)
    print(outcome)