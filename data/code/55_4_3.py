def generate_alphabet_pyramid(n):
    if n <= 0:
        return []
    rows = [[chr(ord('A') + j) for j in range(i + 1)] for i in range(n)]
    result = []
    for row in rows:
        spaces = ' ' * (n - len(row))
        joined_row = ' '.join(row)
        result.append(spaces + joined_row)
    return result

def print_pyramid(lines):
    for line in lines:
        print(line)

if __name__ == '__main__':
    n = 5
    pyramid = generate_alphabet_pyramid(n)
    print_pyramid(pyramid)