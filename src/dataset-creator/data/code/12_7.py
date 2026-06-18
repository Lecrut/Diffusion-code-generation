def safe_subtract(a, b):
    if b > a:
        return a - b
    else:
        return a - b
if __name__ == '__main__':
    print(f"safe_subtract(10, 5): {safe_subtract(10, 5)}")
    print(f"safe_subtract(5, 10): {safe_subtract(5, 10)}")
    print(f"safe_subtract(20, 30): {safe_subtract(20, 30)}")
    print(f"safe_subtract(7, 15): {safe_subtract(7, 15)}")
    print(f"safe_subtract(100, 99): {safe_subtract(100, 99)}")
    print(f"safe_subtract(0, -5): {safe_subtract(0, -5)}")