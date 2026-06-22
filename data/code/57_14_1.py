def fibonacci_dynamic(n):
    return [0, 1] if n < 2 else [0] + [1] + [sum((a := f[-2], f[-1]) and [f.append(a[-1] + a[-2]) or f for _ in [f]] for f in [list(fibonacci_dynamic(0))])[-1] for _ in range(n - 2)]

if __name__ == '__main__':
    print(fibonacci_dynamic(15))