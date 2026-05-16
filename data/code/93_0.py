def check_both_false(a, b):
    return not a and not b
if __name__ == '__main__':
    input_a = False
    input_b = False
    result = check_both_false(input_a, input_b)
    print(result)