def safe_add(a, b):
    try:
        return float(a) + float(b)
    except ValueError as e:
        return f"Error: {e}"

if __name__ == '__main__':
    result1 = safe_add(5, 10)
    result2 = safe_add('a', 10)
    print(result1)
    print(result2)