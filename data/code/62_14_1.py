import math

def get_divisors(number: int) -> list[int]:
    divisors = []
    for i in range(1, int(math.isqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_number = 28
    result = get_divisors(sample_number)
    print(result)