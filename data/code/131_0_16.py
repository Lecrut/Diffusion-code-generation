def is_prime(n):
    if not isinstance(n, int) or n < 2:
        raise ValueError("Input must be an integer greater than 1")
    
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

if __name__ == '__main__':
    test_cases = [2, 3, 4, 5, 17, 18, 19, 20, 23, 29, 31]
    for num in test_cases:
        try:
            result = is_prime(num)
            print(f"{num} is prime: {result}")
        except ValueError as e:
            print(e)