def generate_diamond(height):
    if height <= 0:
        return []
    
    rows = []
    n = (height + 1) // 2
    
    upper_part = [
        (n - 1 - i) * ' ' + (2 * i + 1) * '*' + (n - 1 - i) * ' '
        for i in range(n)
    ]
    
    if height % 2 == 0:
        lower_part = [
            (i) * ' ' + (2 * (n - 1 - i) + 1) * '*' + (i) * ' '
            for i in range(1, n)
        ]
    else:
        lower_part = [
            (i) * ' ' + (2 * (n - 1 - i) + 1) * '*' + (i) * ' '
            for i in range(1, n)
        ]
    
    rows.extend(upper_part)
    rows.extend(lower_part)
    
    return rows

if __name__ == '__main__':
    result = generate_diamond(7)
    for line in result:
        print(line)