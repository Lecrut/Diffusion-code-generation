def get_divisors(n):
    if n == 0:
        return []
    
    divisors = []
    for i in range(1, int(abs(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != abs(n) // i:
                divisors.append(abs(n) // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    result = get_divisors(0)
    print(result)