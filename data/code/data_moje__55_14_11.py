def generate_centered_alphabet_triangle(n=None):
    if n is None:
        n = 5
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for i in range(1, n + 1):
        letters = alphabet[:i]
        line = ''
        for idx, char in enumerate(letters):
            if idx == 0:
                line = char
            else:
                left = letters[:idx][::-1]
                right = letters[idx:]
                line = ''.join(left) + char + ''.join(right)
        padding = ' ' * (n - i)
        result.append(padding + line + padding)
    return result

if __name__ == '__main__':
    lines = generate_centered_alphabet_triangle()
    for line in lines:
        print(line)