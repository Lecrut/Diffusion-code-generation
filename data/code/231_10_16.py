def generate_pattern(n):
    pattern = {'0': 'A', '1': 'B', '2': 'C'}
    return [pattern[str(i % 3)] for i in range(n)]

if __name__ == '__main__':
    print(generate_pattern(10))