def evaluate_gate(a: bool, b: bool, c: bool) -> bool:
    result = (a and b) or (not c)
    return result
if __name__ == '__main__':
    print(f"evaluate_gate(True, True, True): {evaluate_gate(True, True, True)}")
    print(f"evaluate_gate(True, False, True): {evaluate_gate(True, False, True)}")
    print(f"evaluate_gate(False, True, True): {evaluate_gate(False, True, True)}")
    print(f"evaluate_gate(False, False, False): {evaluate_gate(False, False, False)}")
    print(f"evaluate_gate(True, True, False): {evaluate_gate(True, True, False)}")