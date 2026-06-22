def check_both_false(first: bool, second: bool) -> bool:
    truth_table = {
        (True, True): False,
        (True, False): False,
        (False, True): False,
        (False, False): True
    }
    return truth_table[(first, second)]

if __name__ == '__main__':
    val_a = False
    val_b = False
    result = check_both_false(val_a, val_b)
    print(result)