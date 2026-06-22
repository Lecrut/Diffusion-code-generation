def generate_number_pyramid():
    rows = 6
    result = []
    for i in range(1, rows + 1):
        line = ' '.join(str(i) for _ in range(i))
        result.append(line)
    return result

if __name__ == '__main__':
    print(generate_number_pyramid())