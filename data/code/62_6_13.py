def find_divisors(n):
    if n <= 0:
        return []
    
    divisors = set()
    limit = int(n ** 0.5)
    
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
            
    return sorted(list(divisors))

if __name__ == '__main__':
    result = find_divisors(1024)
    print(result)