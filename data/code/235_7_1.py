def generate_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)
if __name__ == '__main__':
    user_input = 5
    generate_pattern(user_input)