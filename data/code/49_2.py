def generate_square(n=7):
    return (n * '*') + '\n' * (n - 1) + (n * '*')

def main():
    result = generate_square(7)
    print(result, end='')

if __name__ == '__main__':
    main()