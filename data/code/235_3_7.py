def print_inverted_pyramid(base_width):
    if base_width % 2 == 0 or base_width < 3:
        raise ValueError("Base width must be an odd number greater than or equal to 3.")
    
    for i in range(base_width, 0, -2):
        spaces = (base_width - i) // 2
        stars = i
        print(' ' * spaces + '*' * stars)

if __name__ == '__main__':
    try:
        print("--- Inverted Pyramid with base width 9 ---")
        print_inverted_pyramid(9)
    except ValueError as e:
        print(e)