def get_divisors(n):
    if n < 1:
        return []
    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(divs)

if __name__ == '__main__':
    sample_value = 100
    result = get_divisors(sample_value)
    print(result)
    
    sample_value2 = 7
    result2 = get_divisors(sample_value2)
    print(result2)