def generate_hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ['*']
    
    top_bottom_row = '*' * size
    middle_row = '*' + ' ' * (size - 2) + '*'
    
    result = []
    result.append(top_bottom_row)
    
    for _ in range(size - 2):
        result.append(middle_row)
    
    if size > 1:
        result.append(top_bottom_row)
    
    return result

if __name__ == '__main__':
    pattern = generate_hollow_square(5)
    print(pattern)
    pattern_small = generate_hollow_square(1)
    print(pattern_small)
    pattern_medium = generate_hollow_square(4)
    print(pattern_medium)