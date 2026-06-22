def generate_reverse_number_triangle(height):
    result = []
    for i in range(height, 0, -1):
        line = " ".join(str(x) for x in range(1, i + 1))
        result.append(line)
    return "\n".join(result)

if __name__ == "__main__":
    print(generate_reverse_number_triangle(4))