def all_true(*args):
    return all(args)
if __name__ == '__main__':
    print(all_true(True, True, True))
    print(all_true(True, False, True))
    print(all_true(False, False))
    print(all_true())
    print(all_true(True))