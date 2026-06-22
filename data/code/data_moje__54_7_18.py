def generate_hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ['*']
    if size == 2:
        return ['**', '**']
    if size == 3:
        return ['***', '* *', '***']
    
    top_bottom = '*' * size
    middle = '*' + ' ' * (size - 2) + '*'
    
    result = [top_bottom]
    for _ in range(size - 2):
        result.append(middle)
    result.append(top_bottom)
    
    return result

if __name__ == '__main__':
    sample_size = 5
    pattern = generate_hollow_square(sample_size)
    for line in pattern:
        print(line)