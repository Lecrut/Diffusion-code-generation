def generate_pattern(n):
    pattern = ['A', 'B', 'C']
    result = []
    for i in range(n):
        result.append(pattern[i % 3])
    return result

if __name__ == '__main__':
    print(generate_pattern(10))