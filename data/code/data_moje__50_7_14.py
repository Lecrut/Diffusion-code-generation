def generate_triangle():
    return "\n".join("*" * i for i in range(1, 21))

if __name__ == '__main__':
    print(generate_triangle())