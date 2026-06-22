def generate_star_square():
    size = 3
    return ("\n".join(("*".join("*" for _ in range(size)) for _ in range(size))),)

if __name__ == '__main__':
    result = generate_star_square()
    print(result[0])