def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_and_print_primes(numbers):
    for num in numbers:
        if is_prime(num):
            print(num)
if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
    find_and_print_primes(sample_set)