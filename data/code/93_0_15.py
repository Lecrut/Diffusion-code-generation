def are_both_false(x: bool, y: bool) -> bool:
    return not x and not y

if __name__ == '__main__':
    sample_a = False
    sample_b = True
    result = are_both_false(sample_a, sample_b)
    print(result)