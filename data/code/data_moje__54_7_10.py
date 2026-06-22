def generate_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    
    top_bottom_row = '*' * n
    middle_row = '*' + ' ' * (n - 2) + '*'
    
    rows = []
    rows.append(top_bottom_row)
    
    for _ in range(n - 2):
        rows.append(middle_row)
    
    if n > 1:
        rows.append(top_bottom_row)
    
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_hollow_square(5))