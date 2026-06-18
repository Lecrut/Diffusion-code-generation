def has_odd_in_generator(gen):
    return any(x % 2 != 0 for x in gen)
if __name__ == '__main__':
    data = [1, 4, 7, 8, 9]
    odd_found = has_odd_in_generator((x ** 2 for x in range(10)))