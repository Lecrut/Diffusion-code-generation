def render_diamond(height):
    if height <= 0:
        return []
    
    half = height // 2
    result = []
    
    for i in range(half + 1):
        spaces = ' ' * (half - i)
        letters = []
        for j in range(2 * i + 1):
            char_code = 65 + min(j, 2 * i - j)
            letters.append(chr(char_code))
        row_str = spaces + ''.join(letters) + spaces
        result.append(row_str)
        
    for i in range(half - 1, -1, -1):
        spaces = ' ' * (half - i)
        letters = []
        for j in range(2 * i + 1):
            char_code = 65 + min(j, 2 * i - j)
            letters.append(chr(char_code))
        row_str = spaces + ''.join(letters) + spaces
        result.append(row_str)
        
    return result

if __name__ == '__main__':
    sample_height = 5
    diamond_pattern = render_diamond(sample_height)
    for line in diamond_pattern:
        print(line)