def generate_alpha_triangle():
    result = []
    for code in range(65, 91):
        line = chr(code) * (code - 64)
        result.append(line)
    return result

if __name__ == '__main__':
    lines = generate_alpha_triangle()
    for line in lines:
        print(line)