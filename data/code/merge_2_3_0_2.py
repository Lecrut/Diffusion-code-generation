def is_even_bitwise(n: int) -> bool:
    return (n & 1) == 0
if __name__ == '__main__':
    samples = [42, -5, 0, 7]
    for val in samples:
        print(f"{val} is {'even' if is_even_bitwise(val) else 'odd'}")