def hollow_square_generator(size):
    if size <= 0:
        return
    if size == 1:
        yield '*'
        return
    
    row_top = '*' * size
    row_bottom = '*' * size
    row_middle = '*' + ' ' * (size - 2) + '*'
    
    yield row_top
    
    for _ in range(size - 2):
        yield row_middle
    
    yield row_bottom

if __name__ == '__main__':
    result = list(hollow_square_generator(5))
    print(result)