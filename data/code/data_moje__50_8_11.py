def generate_star_pyramid(base_width=21):
    if base_width < 1 or base_width % 2 == 0:
        return ""
    
    lines = []
    rows = base_width // 2 + 1
    
    for i in range(rows):
        stars = 2 * i + 1
        spaces = (base_width - stars) // 2
        line = " " * spaces + "*" * stars
        lines.append(line)
    
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_star_pyramid(21)
    print(result)