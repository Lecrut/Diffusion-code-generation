def generate_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        line = ' '.join(str(i) for _ in range(i))
        result.append(line)
    max_len = max(len(line) for line in result)
    aligned = [line.rjust(max_len) for line in result]
    return '\n'.join(aligned)

if __name__ == '__main__':
    print(generate_pyramid(5))