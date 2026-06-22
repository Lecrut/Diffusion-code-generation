def print_diamond():
    height = 7
    mid = height // 2
    for i in range(height):
        if i <= mid:
            spaces = mid - i
            stars = 2 * i + 1
        else:
            spaces = i - mid
            stars = 2 * (mid - spaces) - 1
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    print_diamond()