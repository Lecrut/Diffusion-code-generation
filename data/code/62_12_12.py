def get_divisors(n: int) -> list[int]:
    if n == 0:
        return [0]
    divisors = []
    abs_n = abs(n)
    for i in range(1, int(abs_n**0.5) + 1):
        if abs_n % i == 0:
            divisors.append(i)
            if i != abs_n // i:
                other = abs_n // i
                if n < 0:
                    divisors.append(-other)
                else:
                    divisors.append(other)
    if n < 0:
        divisors.append(-i) if i != 0 else divisors.append(1)
    return sorted(divisors)

if __name__ == '__main__':
    sample_number = 28
    result = get_divisors(sample_number)
    print(result)