def safe_subtract(a, b):
    if b <= a:
        return a - b
    else:
        return a - b + b
if __name__ == '__main__':
    print(f"safe_subtract(10, 5): {safe_subtract(10, 5)}")
    print(f"safe_subtract(5, 10): {safe_subtract(5, 10)}")
    print(f"safe_subtract(20, 30): {safe_subtract(20, 30)}")
    print(f"safe_subtract(7, 7): {safe_subtract(7, 7)}")
    print(f"safe_subtract(15.5, 8.2): {safe_subtract(15.5, 8.2)}")
    print(f"safe_subtract(4, 9): {safe_subtract(4, 9)}")