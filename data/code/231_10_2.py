def generate_pattern(n):
    pattern = ['A', 'B', 'C']
    result = []
    for i in range(n):
        result.append(pattern[i % 3])
    return result

if __name__ == '__main__':
    sample_output = generate_pattern(15)
    print(sample_output)