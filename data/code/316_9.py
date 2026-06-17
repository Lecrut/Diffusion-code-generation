import sys
def draw_inverted_triangle(rows):
    for i in range(rows, 0, -1):
        print("*" * i)
if __name__ == '__main__':
    num_rows = 5
    draw_inverted_triangle(num_rows)