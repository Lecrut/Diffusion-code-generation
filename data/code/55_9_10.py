def generate_mirrored_alphabet_triangle(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(n):
        chars = alphabet[:i+1]
        left = "".join(chars)
        right = "".join(reversed(chars[:-1])) if i > 0 else ""
        line = left + right
        result.append(line)
    return result

if __name__ == '__main__':
    n = 5
    output = generate_mirrored_alphabet_triangle(n)
    for line in output:
        print(line)