FALSE = False

def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    input_a = FALSE
    input_b = FALSE
    result = check_both_false(input_a, input_b)
    print(result)