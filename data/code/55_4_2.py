def generate_pyramid(n):
    if n <= 0:
        return []
    result = []
    for i in range(1, n + 1):
        leading_spaces = ' ' * (n - i)
        chars = ''.join([chr(65 + j) for j in range(i)])
        row = leading_spaces + chars
        result.append(row)
    return result
if __name__ == '__main__':
    pyramid_rows = generate_pyramid(5)
    for row in pyramid_rows:
        print(row)