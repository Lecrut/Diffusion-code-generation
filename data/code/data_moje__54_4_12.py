def construct_hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ['#']
    
    row_str = '#' * size
    inner_row = '#' + ' ' * (size - 2) + '#'
    
    result = [row_str]
    
    for _ in range(size - 2):
        result.append(inner_row)
        
    result.append(row_str)
    
    return result

if __name__ == '__main__':
    h = construct_hollow_square(10)
    for line in h:
        print(line)