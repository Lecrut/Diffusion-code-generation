import random
def check_boolean_a(value):
    return value > 5
def check_boolean_b(value):
    return value % 2 == 0
def compare_results(result_a, result_b):
    if result_a == result_b:
        return "Equal"
    else:
        return "Different"
if __name__ == '__main__':
    value_a = random.randint(1, 10)
    value_b = random.randint(1, 10)
    result_a = check_boolean_a(value_a)
    result_b = check_boolean_b(value_b)
    comparison = compare_results(result_a, result_b)
    print(f"Value A: {value_a}, Result A: {result_a}")
    print(f"Value B: {value_b}, Result B: {result_b}")
    print(f"Comparison: {comparison}")