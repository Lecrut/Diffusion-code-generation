def generate_hollow_square(n):
    return ["".join(['*' if j in (0, n-1) or i in (0, n-1) else ' ' for j in range(n)]) for i in range(n)] if n > 0 else []

if __name__ == '__main__':
    print(generate_hollow_square(5))