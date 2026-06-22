def print_symmetric_reverse_triangle(rows=5):
    for i in range(1, rows + 1):
        num = i
        left_side = []
        while num > 0:
            left_side.append(str(num))
            num -= 1
        left_part = " ".join(left_side)
        right_part = " ".join(left_side[:-1][::-1])
        print(left_part + (" " + right_part if right_part else ""))

if __name__ == '__main__':
    print_symmetric_reverse_triangle(5)