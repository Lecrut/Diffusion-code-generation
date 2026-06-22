EXPONENT = 4
BASE = 3

def compute_power(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    return base ** exponent

if __name__ == '__main__':
    val = compute_power(BASE, EXPONENT)
    print(val)