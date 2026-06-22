def get_divisors(n: int) -> list:
    if n == 0:
        return []
    if n == 1:
        return [1]
    
    divisors = set()
    limit = int(n**0.5)
    
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    
    return sorted(list(divisors))

if __name__ == '__main__':
    print(get_divisors(28))
    print(get_divisors(100))
    print(get_divisors(7))