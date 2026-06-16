def has_odd_in_generator(gen):
    for item in gen:
        if item % 2 != 0:
            return True
    return False
if __name__ == '__main__':
    sample_gen = (x for x in range(1, 10))
    result = has_odd_in_generator(sample_gen)
    print(result)