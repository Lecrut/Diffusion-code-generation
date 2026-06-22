def hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    
    top_and_bottom = '*' * n
    middle_part = '*' + '.' * (n - 2) + '*'
    middle_line = middle_part
    
    top = [top_and_bottom]
    bottom = [top_and_bottom]
    
    if n > 2:
        middle_count = n - 2
        middle = [middle_line] * middle_count
        return top + middle + bottom
    return top + bottom

if __name__ == '__main__':
    for size in [1, 5, 10]:
        result = hollow_square(size)
        for line in result:
            print(line)
        print("---")