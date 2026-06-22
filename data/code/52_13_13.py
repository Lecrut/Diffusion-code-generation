def generate_diamond_pattern(height):
    if height <= 0 or height % 2 == 0:
        raise ValueError("Height must be a positive odd integer")
    
    mid = height // 2
    upper = [' ' * (mid - i) + '*' * (2 * i + 1) for i in range(mid + 1)]
    lower = [' ' * (mid - i) + '*' * (2 * i + 1) for i in range(mid - 1, -1, -1)]
    return '\n'.join(upper + lower)

if __name__ == '__main__':
    result = generate_diamond_pattern(7)
    print(result)