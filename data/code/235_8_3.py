def generate_star_pattern(n):
    result = ""
    for i in range(1, n + 1):
        result += "*" * i + "\n"
    return result
if __name__ == '__main__':
    N = 5
    output = generate_star_pattern(N)
    print(output.rstrip())