def inverted_triangle(n):
    result = []
    for i in range(n):
        stars = '*' * (n - i)
        result.append(stars)
    return '\n'.join(result)

if __name__ == '__main__':
    n = 5
    output = inverted_triangle(n)
    print(output)