def generate_mirrored_triangle(size):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(1, size + 1):
        upper_part = alphabet[:i]
        lower_part = upper_part[::-1][1:]
        line = upper_part + lower_part
        result.append(line)
    return result

if __name__ == '__main__':
    sample_size = 5
    pattern = generate_mirrored_triangle(sample_size)
    for line in pattern:
        print(line)