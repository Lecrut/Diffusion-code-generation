def print_inverted_pyramid(base_width):
    for i in range(base_width // 2, -1, -1):
        print(' ' * (base_width // 2 - i) + '*' * (2 * i + 1))

if __name__ == '__main__':
    pyramid = {
        "base_width": 9
    }
    
    print("--- Inverted Pyramid with Base Width 9 ---")
    print_inverted_pyramid(pyramid["base_width"])