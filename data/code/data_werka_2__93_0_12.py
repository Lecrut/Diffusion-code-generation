def evaluate_boolean_pair(first_flag: bool, second_flag: bool) -> bool:
    status_lookup = {
        (True, True): False,
        (True, False): False,
        (False, True): False,
        (False, False): True,
    }
    return status_lookup[(first_flag, second_flag)]

if __name__ == '__main__':
    val_one = False
    val_two = False
    computed_result = evaluate_boolean_pair(val_one, val_two)
    print(computed_result)