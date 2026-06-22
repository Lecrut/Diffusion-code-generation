def check_both_false(a, b):
    truth_table = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False
    }
    return truth_table[(a, b)]

if __name__ == '__main__':
    val_a = False
    val_b = False
    output = check_both_false(val_a, val_b)
    print(output)