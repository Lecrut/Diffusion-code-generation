def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def extract_prime_position_chars(phrase):
    return ''.join(char for index, char in enumerate(phrase) if is_prime(index + 1))

if __name__ == '__main__':
    sample_phrase = "Hello World"
    print(extract_prime_position_chars(sample_phrase))