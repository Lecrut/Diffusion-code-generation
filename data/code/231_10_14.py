def generate_pattern(n):
    pattern_map = {'A': 0, 'B': 1, 'C': 2}
    result = []
    for i in range(n):
        result.append(list(pattern_map.keys())[pattern_map[list(pattern_map.keys())[i % len(pattern_map)]]])
    return result

if __name__ == '__main__':
    print(generate_pattern(10))