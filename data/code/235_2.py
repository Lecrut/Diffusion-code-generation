def generate_pattern(M):
    lines = [["*" * i] for i in range(1, M + 1)]
    return lines
if __name__ == '__main__':
    M = 5
    pattern = generate_pattern(M)
    for line in pattern:
        print(line)