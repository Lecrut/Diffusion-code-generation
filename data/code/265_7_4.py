def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def extract_prime_position_chars(phrase):
    prime_chars = []
    for index, char in enumerate(phrase, start=1):
        if is_prime(index):
            prime_chars.append(char)
    return ''.join(prime_chars)

if __name__ == '__main__':
    sample_phrase = "Programming is fun!"
    result = extract_prime_position_chars(sample_phrase)
    print(result)