def generate_pyramid(n):
    return ["".join(chr(ord('A') + (i - j) if i - j >= 0 else j - i) for j in range(i + 1)) for i in range(n)]

if __name__ == '__main__':
    result = generate_pyramid(5)
    for row in result:
        print(row)