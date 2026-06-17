import time
def system_a_to_b(input_a):
    time.sleep(0.01)
    if isinstance(input_a, int):
        return input_a * 2
    elif isinstance(input_a, str):
        return input_a.upper()
    else:
        return "Error: Invalid type"
def system_b_to_a(input_b):
    time.sleep(0.01)
    if isinstance(input_b, int):
        return input_b // 2
    elif isinstance(input_b, str):
        return input_b.lower()
    else:
        return "Error: Invalid type"
if __name__ == '__main__':
    sample_input_a = 10
    sample_input_b = "hello world"
    result_a = system_a_to_b(sample_input_a)
    result_b = system_b_to_a(sample_input_b)
    print(f"Input A: {sample_input_a}")
    print(f"Result from System A to B: {result_a}")
    print("-" * 20)
    print(f"Input B: {sample_input_b}")
    print(f"Result from System B to A: {result_b}")