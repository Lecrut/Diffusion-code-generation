def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    if start < 2 or end < 2:
        raise ValueError("Range must be greater than 1")
    if start > end:
        raise ValueError("Start of range must be less than end of range")

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == '__main__':
    print(find_primes_in_range(2, 30))