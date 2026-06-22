def generate_hollow_square(side_length):
    pattern = ""
    for i in range(side_length):
        for j in range(side_length):
            if i == 0 or i == side_length - 1 or j == 0 or j == side_length - 1:
                pattern += "*"
            else:
                pattern += " "
        pattern += "\n"
    return pattern

if __name__ == '__main__':
    print(generate_hollow_square(5))