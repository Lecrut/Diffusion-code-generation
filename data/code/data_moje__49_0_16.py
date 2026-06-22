def generate_solid_square(side_length):
    pattern = ""
    for i in range(side_length):
        for j in range(side_length):
            pattern += "*"
        pattern += "\n"
    return pattern

if __name__ == '__main__':
    result = generate_solid_square(5)
    print(result)