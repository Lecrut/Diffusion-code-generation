def evaluate_false_pair(condition_one: bool, condition_two: bool) -> bool:
    lookup_table = {
        (True, True): False,
        (True, False): False,
        (False, True): False,
        (False, False): True
    }
    return lookup_table[(condition_one, condition_two)]

if __name__ == '__main__':
    val_a = False
    val_b = False
    outcome = evaluate_false_pair(val_a, val_b)
    print(outcome)