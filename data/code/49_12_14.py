def generate_star_grid(size=8):
    if size <= 0:
        return ""
    line = "* " * size
    return "\n".join([line.rstrip()] * size)

if __name__ == '__main__':
    sample_size = 8
    print(generate_star_grid(sample_size))