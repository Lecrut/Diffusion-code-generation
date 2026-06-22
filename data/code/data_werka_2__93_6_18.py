def check_both_false(a, b):
    falsy_values = {0, 0.0, '', [], (), {}, set(), False, None}
    return a in falsy_values and b in falsy_values

if __name__ == '__main__':
    a = 0
    b = None
    result = check_both_false(a, b)
    print(result)