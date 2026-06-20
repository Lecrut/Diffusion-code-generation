def both_false(a: bool, b: bool) -> bool:
    false_values = {False: True}
    return false_values.get(a, False) and false_values.get(b, False)

if __name__ == '__main__':
    result = both_false(False, False)
    print(result)