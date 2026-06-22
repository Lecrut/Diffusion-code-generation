def generate_diamond(size):
    result = []
    for i in range(-size + 1, size):
        num_stars = size - abs(i)
        row = " " * abs(i) + "* " * num_stars
        result.append(row.strip())
    return "\n".join(result)

if __name__ == '__main__':
    size = 5
    print(generate_diamond(size))