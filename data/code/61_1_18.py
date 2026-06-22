def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(n ** 0.5) + 1
    candidates = [2]
    current = 3
    while current <= limit:
        is_divisor = False
        for p in candidates:
            if p * p > current:
                break
            if current % p == 0:
                is_divisor = True
                break
        if not is_divisor:
            candidates.append(current)
            if current * current <= n and n % current == 0:
                return False
            current += 2
        else:
            current += 2
            
    return True

if __name__ == '__main__':
    samples = [1, 2, 3, 4, 17, 18, 97, 100, 7919, 7921]
    for s in samples:
        print(is_prime(s))