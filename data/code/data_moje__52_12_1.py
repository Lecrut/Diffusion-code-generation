def generate_diamond(radius):
    if radius <= 0:
        return ""
    lines = []
    for i in range(-radius, radius + 1):
        spaces = abs(i)
        stars = 2 * (radius - spaces) + 1
        lines.append(" " * spaces + "*" * stars)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_radius = 5
    print(generate_diamond(sample_radius))