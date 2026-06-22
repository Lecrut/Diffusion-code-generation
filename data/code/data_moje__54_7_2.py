def generate_hollow_square(n):
    if n <= 0:
        return []
    
    top_bottom_row = '+' + '-' * (n - 2) + '+'
    if n > 2:
        middle_row = '|' + ' ' * (n - 2) + '|'
    elif n == 2:
        middle_row = '++'
    else:
        middle_row = '+'
    
    rows = []
    rows.append(top_bottom_row)
    
    if n > 2:
        for _ in range(n - 2):
            rows.append(middle_row)
        
        rows.append(top_bottom_row)
    elif n == 2:
        rows.append(top_bottom_row)
    elif n == 1:
        rows.append('+')
    
    return rows

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print('\n'.join(result))