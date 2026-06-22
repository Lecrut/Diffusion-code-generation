def generate_square_pattern(size):
    line = "* " * size
    result = ("\n" + line).join([""] * size)
    return result.strip()

if __name__ == '__main__':
    print(generate_square_pattern(12))