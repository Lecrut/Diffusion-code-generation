def print_diamond(height: int = 7) -> str:
    if height % 2 == 0:
        raise ValueError("Height must be an odd number for a symmetric diamond")
    
    mid = height // 2
    lines = []
    
    for i in range(-mid, mid + 1):
        spaces = ' ' * (mid - abs(i))
        stars = '*' * (2 * abs(i) + 1)
        lines.append(spaces + stars)
    
    diamond_str = '\n'.join(lines)
    print(diamond_str)
    return diamond_str

if __name__ == '__main__':
    result = print_diamond(7)