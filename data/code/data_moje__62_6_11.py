import math

def compute_divisors(target):
    if not isinstance(target, int):
        raise TypeError("Input must be an integer")
    if target < 1:
        raise ValueError("Input must be a positive integer")
    divs = set()
    boundary = math.isqrt(target)
    for candidate in range(1, boundary + 1):
        if target % candidate == 0:
            divs.add(candidate)
            divs.add(target // candidate)
    return sorted(divs)

if __name__ == '__main__':
    num = 1024
    ans = compute_divisors(num)
    print(ans)