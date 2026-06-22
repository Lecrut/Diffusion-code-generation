import sys

def generate_diamond_pattern(n: int) -> str:
    if n <= 0:
        return ""
    
    lines = []
    middle = n - 1
    
    for i in range(n):
        spaces = ' ' * (middle - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (middle - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_size = 5
    print(generate_diamond_pattern(sample_size))