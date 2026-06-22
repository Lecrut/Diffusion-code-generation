def generate_diamond(size):
    if size <= 0:
        return ""
    
    half = size // 2
    result = []
    
    for i in range(half, -1, -1):
        spaces = ' ' * i
        stars = '*' * (size - 2 * i)
        result.append(spaces + stars)
    
    for i in range(1, half + 1):
        spaces = ' ' * i
        stars = '*' * (size - 2 * i)
        result.append(spaces + stars)
    
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_diamond(5))