def generate_number_pyramid(height=5):
    result = []
    for i in range(1, height + 1):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))
        result.append(" ".join(row))
    return result

if __name__ == '__main__':
    print(generate_number_pyramid())