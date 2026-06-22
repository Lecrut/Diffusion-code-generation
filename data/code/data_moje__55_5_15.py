def get_diamond_alphabet(height):
    if height < 1:
        return []
    
    n = (height + 1) // 2
    lines = []
    
    for i in range(1, n + 1):
        char_val = 64 + i
        char = chr(char_val)
        spaces = n - i
        line = ' ' * spaces + char * (2 * i - 1) + ' ' * spaces
        lines.append(line)
    
    for i in range(n - 1, 0, -1):
        char_val = 64 + i
        char = chr(char_val)
        spaces = n - i
        line = ' ' * spaces + char * (2 * i - 1) + ' ' * spaces
        lines.append(line)
    
    return lines

if __name__ == '__main__':
    result = get_diamond_alphabet(9)
    for line in result:
        print(line)