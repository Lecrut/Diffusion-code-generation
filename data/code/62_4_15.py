NUM = 60
THRESHOLD = NUM

def get_divisors(n):
    large_divs = []
    small_divs = []
    limit = int(n**0.5)
    for i in range(1, limit + 1):
        if n % i == 0:
            small_divs.append(i)
            if i * i != n:
                large_divs.append(n // i)
    large_divs.reverse()
    return small_divs + large_divs

if __name__ == '__main__':
    result = get_divisors(NUM)
    print(result)