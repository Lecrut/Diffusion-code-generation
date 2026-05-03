def compare_and_report(num1: float, num2: float) -> bool:
    result = num1 < num2
    return result
if __name__ == '__main__':
    a = 5.0
    b = 10.0
    print(f"Comparing {a} and {b}: {compare_and_report(a, b)}")
    c = 10.0
    d = 5.0
    print(f"Comparing {c} and {d}: {compare_and_report(c, d)}")
    e = 7.5
    f = 7.5
    print(f"Comparing {e} and {f}: {compare_and_report(e, f)}")