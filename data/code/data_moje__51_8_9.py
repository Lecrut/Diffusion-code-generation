def generate_number_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        line = str(i) * i
        result.append(line)
    return result

if __name__ == '__main__':
    rows = 5
    pyramid = generate_number_pyramid(rows)
    for line in pyramid:
        print(line)