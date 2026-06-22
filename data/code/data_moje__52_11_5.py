def generate_diamond(size):
    if size < 1 or size % 2 == 0:
        return []
    
    half = size // 2
    rows = []
    
    for i in range(half + 1):
        spaces = half - i
        stars = 2 * i + 1
        line = ' ' * spaces + '*' * stars
        rows.append(line)
    
    for i in range(half - 1, -1, -1):
        spaces = half - i
        stars = 2 * i + 1
        line = ' ' * spaces + '*' * stars
        rows.append(line)
    
    return rows

if __name__ == '__main__':
    dimensions = 5
    result = generate_diamond(dimensions)
    for row in result:
        print(row)