def display_inverted_triangle(height=5):
    for i in range(height, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    display_inverted_triangle(5)