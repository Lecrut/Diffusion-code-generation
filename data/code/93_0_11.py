def evaluate_booleans(x: bool, y: bool) -> bool:
    result = not x and not y
    return result

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    outcome = evaluate_booleans(sample_a, sample_b)
    print(outcome)