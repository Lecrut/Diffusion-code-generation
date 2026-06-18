import sys
def compute_sum(a: float, b: float, c: float) -> float:
    return a + b + c
if __name__ == '__main__':
    val_a = 10.5
    val_b = -3.2
    val_c = 7.8
    try:
        result = compute_sum(val_a, val_b, val_c)
        print(result)
    except TypeError as e:
        sys.stderr.write(f"Error: {e}\n")