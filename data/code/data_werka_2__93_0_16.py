def evaluate_dual_boolean_state(first_val, second_val):
    state_map = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False
    }
    return state_map[(first_val, second_val)]

if __name__ == '__main__':
    val_one = False
    val_two = False
    status = evaluate_dual_boolean_state(val_one, val_two)
    print(status)