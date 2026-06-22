def generate_alphabet_triangle(n):
    letters = [chr(ord('A') + i) for i in range(n)]
    result = []
    for i in range(n):
        row = (letters[: i + 1] + letters[:i][::-1])
        result.append(' '.join(row))
    return '\n'.join(result)

if __name__ == '__main__':
    n = 5
    print(generate_alphabet_triangle(n))