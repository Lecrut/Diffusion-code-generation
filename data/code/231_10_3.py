def generate_pattern(n):
    return ['A', 'B', 'C'] * ((n // 3) + (1 if n % 3 else 0))[:n]

if __name__ == '__main__':
    print(generate_pattern(10))