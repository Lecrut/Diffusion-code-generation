def reverse_integer(n: int) -> int:
    if n < 0:
        reversed_str = "-" + str(n)[::-1].replace("-", "")
    else:
        reversed_str = str(n)[::-1]
    result = int(reversed_str)
    return result

if __name__ == '__main__':
    test_values = [123, -456, 0, 1200, -100]
    for val in test_values:
        print(reverse_integer(val))