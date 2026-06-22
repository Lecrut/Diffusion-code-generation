def check_even(value):
    if not isinstance(value, int) or isinstance(value, bool):
        return None
    return value % 2 == 0

if __name__ == '__main__':
    results = []
    results.append(check_even(4))
    results.append(check_even(5))
    results.append(check_even("hello"))
    for res in results:
        print(res)