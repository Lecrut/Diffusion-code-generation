def compare_large_integers(a, b):
    if not isinstance(a, (int, list)) or not isinstance(b, (int, list)):
        raise ValueError("Both arguments must be either an integer or a list of integers")

    size_a = len(a) if isinstance(a, list) else 1
    size_b = len(b) if isinstance(b, list) else 1

    if size_a > size_b:
        return (a, "greater")
    elif size_b > size_a:
        return (b, "greater")
    else:
        return (a, "equal")

if __name__ == '__main__':
    num1 = [1000000]
    num2 = [10, 20, 30]

    result1 = compare_large_integers(num1, num2)
    print(result1)

    num3 = [1, 2, 3]
    num4 = [4, 5]

    result2 = compare_large_integers(num3, num4)
    print(result2)

    num5 = 123456789
    num6 = [987654321]

    result3 = compare_large_integers(num5, num6)
    print(result3)