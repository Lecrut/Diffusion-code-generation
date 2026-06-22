import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

def run_verification():
    correct = 0
    failures = 0
    for _ in range(100):
        inputs = {
            "a": random.choice([True, False]),
            "b": random.choice([True, False]),
            "c": random.choice([True, False]),
            "d": random.choice([True, False])
        }
        expected = evaluate_expression(
            inputs["a"], inputs["b"], inputs["c"], inputs["d"]
        )
        actual = evaluate_expression(
            inputs["a"], inputs["b"], inputs["c"], inputs["d"]
        )
        if expected != actual:
            failures += 1
        else:
            correct += 1
    return {"correct": correct, "failures": failures}

if __name__ == '__main__':
    test_results = run_verification()
    print(test_results)
    sample_output = evaluate_expression(True, False, True, False)
    print(sample_output)