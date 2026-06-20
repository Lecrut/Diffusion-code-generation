def check_equivalence(a: bool, b: bool) -> str:
    if a == b:
        return 'Equal'
    else:
        return 'One is True, the other is False'

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = check_equivalence(sample_a, sample_b)
    print(result)