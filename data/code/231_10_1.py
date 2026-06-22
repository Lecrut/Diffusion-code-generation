def generate_pattern(n):
    pattern = ['A', 'B', 'C']
    return [pattern[i % 3] for i in range(n)]

if __name__ == '__main__':
    print(generate_pattern(10))