def get_divisors(n):
    return sorted(i for i in range(1, int(n**0.5) + 1) if n % i == 0 for i in (i, n // i) if i <= n // i)

def divisors_of_60():
    return get_divisors(60)

if __name__ == '__main__':
    print(divisors_of_60())