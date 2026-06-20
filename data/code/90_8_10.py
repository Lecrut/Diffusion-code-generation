THRESHOLD_A = 5
THRESHOLD_B = 10

def evaluate_or_condition(a, b):
    return (a > THRESHOLD_A) or (b < THRESHOLD_B)

if __name__ == '__main__':
    sample_a = 6
    sample_b = 9
    result = evaluate_or_condition(sample_a, sample_b)
    print(result)