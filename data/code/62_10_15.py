from typing import List

def get_divisors(number: int) -> List[int]:
    if number == 0:
        return []
    if number < 0:
        number = -number
    divisors = set()
    step = 1 if number % 2 != 0 else 2
    limit = int(number ** 0.5)
    for i in range(1, limit + 1, 1 if number % 2 != 0 else 2 if i == 1 else 2):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
    return sorted(list(divisors))

if __name__ == '__main__':
    sample_number = 84
    result = get_divisors(sample_number)
    print(result)