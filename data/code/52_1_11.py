def print_diamond(height=7):
    if height % 2 == 0 or height <= 0:
        return

    mid = height // 2
    for i in range(mid + 1):
        spaces = mid - i
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)

    for i in range(mid - 1, -1, -1):
        spaces = mid - i
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)

if __name__ == "__main__":
    print_diamond(7)