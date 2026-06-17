def generate_pattern(n=100):
    pattern = []
    for i in range(n):
        index = i % 3
        value = 7 + 7 * index
        pattern.append(value)
    return pattern
if __name__ == '__main__':
    result = generate_pattern()
    print(result)