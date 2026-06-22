def generate_hollow_square(n):
    if n < 1:
        return []
    if n == 1:
        return ['*']
    top_bottom = '*' + ' ' * (n - 2) + '*'
    middle = '*' + ' ' * (n - 2) + '*'
    result = [top_bottom]
    for _ in range(n - 2):
        result.append('*' + ' ' * (n - 2) + '*')
    result.append(top_bottom)
    return result

if __name__ == '__main__':
    print(generate_hollow_square(5))