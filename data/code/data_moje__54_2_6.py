def generate_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    
    top_bottom = '*' * n
    middle_inner = '*' + ' ' * (n - 2) + '*'
    
    return [top_bottom] + [middle_inner for _ in range(n - 2)] + [top_bottom]

if __name__ == '__main__':
    print(generate_hollow_square(5))