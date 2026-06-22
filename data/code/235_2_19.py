def draw_diamond():
    for i in range(5):
        spaces = " " * (4 - abs(i - 2))
        bars = "|" * (i + 1)
        print(spaces + bars)

if __name__ == '__main__':
    draw_diamond()