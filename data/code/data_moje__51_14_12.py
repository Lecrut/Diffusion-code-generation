def generate_number_pyramid(height):
    result = []
    for i in range(1, height + 1):
        row = ""
        for j in range(1, i + 1):
            row += str(j)
        result.append(row)
    return result

if __name__ == '__main__':
    pyramid_height = 5
    pyramid = generate_number_pyramid(pyramid_height)
    print(pyramid)