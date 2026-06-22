def generate_number_pyramid(height=5):
    result = []
    for i in range(1, height + 1):
        row = str(i).join([''] + [str(i)] * (i - 1)).lstrip()
        result.append(row)
    return result

if __name__ == '__main__':
    pyramid = generate_number_pyramid()
    print(pyramid)