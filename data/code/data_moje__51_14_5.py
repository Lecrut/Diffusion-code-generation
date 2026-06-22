def generate_number_pyramid(height):
    result = []
    for i in range(1, height + 1):
        row_numbers = [str(j) for j in range(1, 2 * i)]
        row_center = len("".join(row_numbers))
        row_str = " " * ((height - i) * 2) + " ".join(row_numbers)
        padded = row_str.center((height * 2 - 1) * 2)
        result.append(padded)
    return result

if __name__ == '__main__':
    height = 5
    pyramid = generate_number_pyramid(height)
    for line in pyramid:
        print(line)