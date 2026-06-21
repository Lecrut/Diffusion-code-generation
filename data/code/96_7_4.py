import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

def test_expression():
    num_tests = 100
    all_passed = True
    for _ in range(num_tests):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        expected = (a and b) or (c and not d)
        result = evaluate_expression(a, b, c, d)
        if result != expected:
            all_passed = False
            break
    return all_passed

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    sample_result = evaluate_expression(sample_a, sample_b, sample_c, sample_d)
    print(sample_result)
    
    test_result = test_expression()
    print(test_result)