def is_odd(n):
    return n & 1 != 0
def main():
    test_values = [5, -3, 42, 0]
    for val in test_values:
        print(f"{val} is {'odd' if is_odd(val) else 'even'}")
if __name__ == '__main__':
    main()