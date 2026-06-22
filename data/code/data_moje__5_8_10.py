import math

def compare_lengths(a: float, b: float) -> tuple:
    diff = abs(a - b)
    if a > b:
        return (diff, "First is greater")
    elif b > a:
        return (diff, "Second is greater")
    else:
        return (diff, "Equal")

if __name__ == '__main__':
    result = compare_lengths(10.5, 8.2)
    print(result)