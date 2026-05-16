def evaluate_inequality(x, y):
    try:
        return x <= y
    except TypeError:
        return False
if __name__ == '__main__':
    print(f"evaluate_inequality(5, 10): {evaluate_inequality(5, 10)}")
    print(f"evaluate_inequality(10, 10): {evaluate_inequality(10, 10)}")
    print(f"evaluate_inequality(12, 8): {evaluate_inequality(12, 8)}")
    print(f"evaluate_inequality('a', 5): {evaluate_inequality('a', 5)}")
    print(f"evaluate_inequality(5, 'b'): {evaluate_inequality(5, 'b')}")
    print(f"evaluate_inequality(None, 5): {evaluate_inequality(None, 5)}")
    print(f"evaluate_inequality(None, None): {evaluate_inequality(None, None)}")