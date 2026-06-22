def generate_number_pyramid(height):
    result = []
    for i in range(1, height + 1):
        row = [str(i)] * i
        result.append(" ".join(row))
    return result

if __name__ == '__main__':
    print(generate_number_pyramid(5))