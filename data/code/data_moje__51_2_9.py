def generate_number_pyramid():
    rows = 6
    result = []
    current_number = 1
    for i in range(1, rows + 1):
        row_numbers = []
        for _ in range(i):
            row_numbers.append(str(current_number))
            current_number += 1
        result.append(" ".join(row_numbers))
    return result

if __name__ == '__main__':
    pyramid = generate_number_pyramid()
    for line in pyramid:
        print(line)