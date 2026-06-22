def get_divisors(n: int) -> list[int]:
    if n == 0:
        return []
    
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i and n // i != n:
                other = n // i
                if other > 0:
                    divisors.append(other)
    
    return sorted(divisors)

if __name__ == '__main__':
    sample_number = 12
    result = get_divisors(sample_number)
    print(result)