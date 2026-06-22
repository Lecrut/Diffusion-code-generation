import string

def alphabet_triangle(n):
    if n <= 0:
        return ''
    lines = []
    alphabet = string.ascii_uppercase
    for i in range(1, n + 1):
        line = alphabet[:i]
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = alphabet_triangle(5)
    print(result)