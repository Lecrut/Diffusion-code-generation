import random
def check_condition_a(value):
    return value > 5
def check_condition_b(value):
    return value % 2 == 0
def simulate_and_compare():
    value_a = random.randint(1, 10)
    value_b = random.randint(1, 10)
    result_a = check_condition_a(value_a)
    result_b = check_condition_b(value_b)
    comparison_result = result_a == result_b
    print(f"Value A: {value_a}, Result A: {result_a}")
    print(f"Value B: {value_b}, Result B: {result_b}")
    print(f"Comparison (A == B): {comparison_result}")
if __name__ == '__main__':
    simulate_and_compare()