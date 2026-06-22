def generate_star_grid(size=8):
    return "\n".join(["*" * size] * size)

if __name__ == '__main__':
    print(generate_star_grid())
    print(generate_star_grid(5))