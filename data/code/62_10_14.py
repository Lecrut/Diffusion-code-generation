def get_sorted_divisors(n: int) -> list[int]:
    if n <= 0:
        return []
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(list(divisors))

if __name__ == '__main__':
    sample_numbers = [12, 1, 13, 36, 100]
    for num in sample_numbers:
        result = get_sorted_divisors(num)
        print(result)