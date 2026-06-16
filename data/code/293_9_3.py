import time
def system_a_to_b(value_a):
    time.sleep(0.001)
    if isinstance(value_a, int):
        return value_a * 2
    elif isinstance(value_a, str):
        return value_a.upper()
    else:
        return "Error: Unsupported type"
def system_b_to_a(value_b):
    time.sleep(0.001)
    if isinstance(value_b, int):
        return value_b // 2
    elif isinstance(value_b, str):
        return value_b.lower()
    else:
        return "Error: Unsupported type"
if __name__ == '__main__':
    sample_input_a = 10
    sample_input_b = "hello world"
    result_b = system_a_to_b(sample_input_a)
    result_a = system_b_to_a(result_b)
    print(f"Input A: {sample_input_a}")
    print(f"Intermediate Result (A -> B): {result_b}")
    print(f"Final Result (B -> A): {result_a}")