def generate_pattern(n=100):
    pattern = [7, 14, 21]
    result = []
    for i in range(n):
        index = i % 3
        result.append(pattern[index])
    return result
if __name__ == '__main__':
    print(generate_pattern())