def generate_hollow_square(side):
    top_row = '#' * side
    middle_row = '#' + '.' * (side - 2) + '#' if side > 2 else '#'
    
    yield top_row
    
    for _ in range(side - 2):
        yield middle_row
        
    if side > 1:
        yield top_row

if __name__ == '__main__':
    result = list(generate_hollow_square(5))
    print(result)