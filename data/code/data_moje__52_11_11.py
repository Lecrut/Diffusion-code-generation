def generate_diamond_pattern(max_height):
    if max_height < 1 or max_height % 2 == 0:
        raise ValueError("max_height must be a positive odd integer")
    
    result = []
    mid = max_height // 2
    
    for i in range(-mid, mid + 1):
        spaces = abs(i)
        stars = max_height - 2 * spaces
        line = " " * spaces + "*" * stars
        result.append(line)
    
    return "\n".join(result)

if __name__ == '__main__':
    sample_height = 7
    print(generate_diamond_pattern(sample_height))