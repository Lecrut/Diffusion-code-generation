def generate_alphabet_pyramid(n):
    if n <= 0:
        return []
    
    pattern = []
    for i in range(n):
        row = [chr(ord('A') + j) for j in range(i + 1)]
        spaces = ' ' * (n - i - 1)
        full_row = spaces + ' '.join(row) + spaces
        pattern.append(full_row)
    return pattern

def format_pyramid(pattern):
    if not pattern:
        return ""
    return '\n'.join(pattern)

if __name__ == '__main__':
    n = 5
    pyramid = generate_alphabet_pyramid(n)
    result = format_pyramid(pyramid)
    print(result)