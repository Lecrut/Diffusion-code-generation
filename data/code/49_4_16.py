def generate_star_square():
    lines = []
    for _ in range(4):
        lines.append("* * * *")
    return lines

if __name__ == "__main__":
    result = generate_star_square()
    for line in result:
        print(line)