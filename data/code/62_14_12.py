def get_divisors(number: int) -> list[int]:
    if number <= 0:
        return []
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sorted(divisors)

if __name__ == '__main__':
    n = 28
    result = get_divisors(n)
    print(result)