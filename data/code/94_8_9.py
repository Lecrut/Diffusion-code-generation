def check_any_true(iterable):
    for value in iterable:
        if value:
            return True
    return False

if __name__ == '__main__':
    test_values = [False, 0, '', None, [], (), set(), {}, 'hello']
    result = check_any_true(test_values)
    print(result)