def both_false_gen(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    result = (not a) and (not b)
    yield result

if __name__ == '__main__':
    sample_a = False
    sample_b = False
    generator = both_false_gen(sample_a, sample_b)
    result = next(generator)
    print(result)