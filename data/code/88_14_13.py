def both_truthy(a, b):
    return bool(a) and bool(b)

if __name__ == '__main__':
    print(both_truthy(True, False))
    print(both_truthy(0, 1))
    print(both_truthy("hello", ""))
    print(both_truthy({}, {"key": "value"}))