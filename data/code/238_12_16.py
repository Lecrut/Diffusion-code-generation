def render_diamond():
    size = 7
    center = size // 2
    
    for i in range(size):
        if i < center:
            num_pluses = (i * 2) + 1
            leading_spaces = center - i
        else:
            num_pluses = ((size - 1) - i) * 2 + 1
            leading_spaces = i - center
        
        line = " " * leading_spaces + "+" * num_pluses
        print(line)

if __name__ == '__main__':
    render_diamond()