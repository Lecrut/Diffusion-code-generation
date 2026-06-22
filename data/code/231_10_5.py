PATTERN = ['A', 'B', 'C']

def generate_pattern(n):
    return [PATTERN[i % 3] for i in range(n)]

if __name__ == '__main__':
    print(generate_pattern(10))