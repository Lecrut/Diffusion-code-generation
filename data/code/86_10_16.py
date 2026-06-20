def compare_booleans(a: bool, b: bool) -> str:
    outcome = 'Equal' if a == b else 'Different'
    return outcome

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    print(compare_booleans(sample_a, sample_b))
    print(compare_booleans(not sample_a, not sample_b))
    print(compare_booleans(sample_a, not sample_b))
    print(compare_booleans(not sample_a, sample_b))