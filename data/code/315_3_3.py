def generate_sequence(n):
    sequence = "ABCDE"
    repeats = n // 5
    remainder = n % 5
    result = sequence * repeats + sequence[:remainder]
    return result
if __name__ == '__main__':
    print(generate_sequence(0))
    print(generate_sequence(1))
    print(generate_sequence(5))
    print(generate_sequence(6))
    print(generate_sequence(10))
    print(generate_sequence(12))