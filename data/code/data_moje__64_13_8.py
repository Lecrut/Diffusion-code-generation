def power(base: int, exp: int, mod: int = None) -> int:
    if exp < 0:
        if mod is None:
            raise ValueError("Negative exponent requires modular inverse support")
        base = pow(base, -1, mod)
        exp = -exp
    
    result = 1
    current_base = base % mod if mod else base
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * current_base) % mod if mod else result * current_base
        exp = exp >> 1
        current_base = (current_base * current_base) % mod if mod else current_base * current_base
    
    if mod:
        return result % mod
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 10, 1000))
    print(power(5, 0, 100))
    print(power(7, 5))
    print(power(10, 100, 1000000007))