def reverse_order(a: float, b: float) -> (float, float):
    return b, a

if __name__ == '__main__':
    result = reverse_order(3.14, 2.71)
    print(result)