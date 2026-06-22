def generate_arrowhead(width):
    if width % 2 == 0:
        raise ValueError("Width must be odd")
    
    half_width = (width - 1) // 2
    arrowhead = []
    
    for i in range(half_width + 1):
        row = [' '] * width
        row[half_width - i] = '/'
        row[half_width + i] = '\\'
        arrowhead.append(''.join(row))
    
    return '\n'.join(arrowhead)

if __name__ == '__main__':
    print(generate_arrowhead(5))