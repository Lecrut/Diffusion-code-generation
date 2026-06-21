def check_both_false(a, b):
    def is_falsy(val):
        return not val
    return is_falsy(a) and is_falsy(b)
if __name__ == '__main__':
    a = 0
    b = []
    result = check_both_false(a, b)
    print(result)