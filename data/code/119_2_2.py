def reverse_order(a: int, b: int) -> tuple:
    return (b, a)

if __name__ == '__main__':
    result = reverse_order(42, 24)
    print(result)