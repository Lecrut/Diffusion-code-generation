def both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    sample_a = False
    sample_b = True
    result = both_false(sample_a, sample_b)
    print(result)