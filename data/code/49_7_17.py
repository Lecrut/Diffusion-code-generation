def generate_star_square(n):
    return ["".join("*" for _ in range(n)) for _ in range(n)]

if __name__ == '__main__':
    result = generate_star_square(3)
    for row in result:
        print(row)