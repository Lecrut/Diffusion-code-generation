def validate_base_width(base_width):
    if base_width % 2 == 0 or base_width < 1:
        raise ValueError("Base width must be an odd number greater than 0")

def print_inverted_pyramid(base_width):
    validate_base_width(base_width)
    half_height = (base_width + 1) // 2
    for i in range(half_height, 0, -1):
        spaces = half_height - i
        stars = base_width - 2 * spaces
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    print_inverted_pyramid(9)