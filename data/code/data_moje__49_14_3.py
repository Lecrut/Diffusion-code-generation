def generate_star_pattern(side_length: int = 7) -> list:
    pattern = []
    for _ in range(side_length):
        pattern.append('*' * side_length)
    return pattern

if __name__ == '__main__':
    side = 7
    result = generate_star_pattern(side)
    for line in result:
        print(line)