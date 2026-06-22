def print_inverted_pyramid(width):
    if not isinstance(width, int) or width % 2 == 0 or width < 1:
        raise ValueError("Width must be an odd integer greater than 0.")
    
    for i in range(width // 2 + 1):
        stars = "*" * (width - 2 * i)
        spaces = " " * i
        print(spaces + stars)

if __name__ == '__main__':
    try:
        print("--- Inverted Pyramid with Base Width 9 ---")
        print_inverted_pyramid(9)
    except ValueError as e:
        print(e)