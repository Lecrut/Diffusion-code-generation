def both_false_generator(a, b):
    yield a is False and b is False

if __name__ == '__main__':
    result = list(both_false_generator(False, False))
    print(result)