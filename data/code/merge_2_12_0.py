def is_odd(n: int) -> bool:
    return (n & 1) != 0
if __name__ == '__main__':
    samples = [-5, -4, 0, 32768, 999]
    for val in samples:
        result = is_odd(val)
        print(f"{val} is {'odd' if result else 'even'}")