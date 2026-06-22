def render_diamond(height):
    if height % 2 == 0:
        upper_half = height // 2
        lower_half = height // 2
    else:
        upper_half = height // 2
        lower_half = height // 2
    
    mid = upper_half
    lines = []
    
    for i in range(height):
        if i <= mid:
            spaces = mid - i
            stars = 2 * i + 1
        else:
            spaces = i - mid
            stars = 2 * (height - i - 1) + 1
        
        line = ' ' * spaces + '* ' * (stars // 2) + '*'
        if stars > 0:
            line = ' ' * spaces + ('* ' * (stars // 2)) + '*'
        else:
            line = '*'
        
        lines.append(line)
        
    return '\n'.join(lines)

if __name__ == '__main__':
    print(render_diamond(7))