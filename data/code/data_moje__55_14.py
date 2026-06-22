def generate_alphabet_triangle():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for i in range(len(letters)):
        line = letters[:i + 1]
        padding = ' ' * (len(letters) - 1 - i)
        result.append(padding + line + ' ' + line[::-1] if i > 0 else padding + line)
    return result

if __name__ == '__main__':
    pattern = generate_alphabet_triangle()
    for line in pattern:
        print(line)