def generate_star_square():
    lines = []
    for _ in range(4):
        lines.append('*' * 4)
    return lines

if __name__ == '__main__':
    result = generate_star_square()
    print(result)