def print_left_aligned_triangle(rows):
    star = ""
    for _ in range(rows):
        star += "*"
        print(star)

if __name__ == '__main__':
    print_left_aligned_triangle(15)