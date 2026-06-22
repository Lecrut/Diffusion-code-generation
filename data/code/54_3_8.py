def generate_hollow_square(n, char='#'):
    if n <= 0:
        return []
    if n == 1:
        return [char]
    
    result = []
    top_bottom = char * n
    middle = char + ' ' * (n - 2) + char
    
    for i in range(n):
        if i == 0 or i == n - 1:
            result.append(top_bottom)
        else:
            result.append(middle)
            
    return result

if __name__ == '__main__':
    output = generate_hollow_square(5, '*')
    print(output)