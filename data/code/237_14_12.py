def generate_sequence(n):
    return [2**i for i in range(n)]

if __name__ == '__main__':
    print(generate_sequence(5))