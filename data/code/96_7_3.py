import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

def run_tests():
    correct_count = 0
    total_tests = 100
    
    for _ in range(total_tests):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        
        expected = (a and b) or (c and not d)
        result = evaluate_expression(a, b, c, d)
        
        if result != expected:
            raise AssertionError(f"Failed for a={a}, b={b}, c={c}, d={d}: expected {expected}, got {result}")
        correct_count += 1
    
    return correct_count

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    
    sample_result = evaluate_expression(sample_a, sample_b, sample_c, sample_d)
    print(f"Sample result: {sample_result}")
    
    test_count = run_tests()
    print(f"Tests passed: {test_count}")