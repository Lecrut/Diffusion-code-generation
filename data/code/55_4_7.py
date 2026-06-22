def generate_alphabet_pyramid(n):
    letters = [chr(ord('A') + i) for i in range(n)]
    lines = [''.join(letters[:i + 1]) for i in range(n)]
    return lines

if __name__ == '__main__':
    result = generate_alphabet_pyramid(5)
    for line in result:
        print(line)