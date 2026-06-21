def first_element(gen):
    iterator = iter(gen)
    return next(iterator)

if __name__ == '__main__':
    gen = (x for x in [10, 20, 30])
    result = first_element(gen)
    print(result)