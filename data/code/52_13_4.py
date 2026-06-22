def generate_diamond(height: int) -> list[str]:
    if height <= 0:
        return []
    
    half = height // 2
    pattern = []
    
    for i in range(half + 1):
        spaces = ' ' * (half - i)
        stars = '*' * (2 * i + 1)
        pattern.append(f"{spaces}{stars}{spaces}")
    
    for i in range(half - 1, -1, -1):
        spaces = ' ' * (half - i)
        stars = '*' * (2 * i + 1)
        pattern.append(f"{spaces}{stars}{spaces}")
    
    return pattern

def print_diamond(pattern: list[str]) -> str:
    return '\n'.join(pattern)

if __name__ == '__main__':
    height = 5
    pattern = generate_diamond(height)
    result = print_diamond(pattern)
    print(result)