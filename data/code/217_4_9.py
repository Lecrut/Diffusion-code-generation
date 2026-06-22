def compare_numbers(a, b):
    return f"a {'>=' if a == b else '>' if a > b else '<'} b"

if __name__ == '__main__':
    print(compare_numbers(5, 3))
    print(compare_numbers(2, 4))
    print(compare_numbers(7, 7))