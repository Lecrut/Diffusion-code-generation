def generate_star_square(size=3):
    return ("*".join(["*"] * size) for _ in range(size))

if __name__ == '__main__':
    rows = generate_star_square()
    for row in rows:
        print(row)