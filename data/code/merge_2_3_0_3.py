def is_even(n):
    return (n & 1) == 0
if __name__ == '__main__':
    for val in [256, -3, 4096, -8]:
        print(f"{val} is {'even' if is_even(val) else 'odd'}")