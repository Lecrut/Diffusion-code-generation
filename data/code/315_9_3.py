def generate_pattern(n):
    pattern = [7, 14, 21]
    result = []
    for i in range(n):
        result.append(pattern[i % 3])
    return result
if __name__ == '__main__':
    print(generate_pattern(100))