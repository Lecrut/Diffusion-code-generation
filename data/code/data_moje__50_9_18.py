def display_inverted_triangle():
    height = 5
    for i in range(height):
        row = ' *' * (height - i)
        print(row)

if __name__ == '__main__':
    display_inverted_triangle()