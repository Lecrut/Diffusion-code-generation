def print_diamond(height):
    if height <= 0:
        return
    mid = height // 2
    top_part = [((2 * i + 1) * '*').center(2 * mid + 1) for i in range(mid + 1)]
    bottom_part = [row for row in top_part[-2::-1]]
    full_diamond = top_part + bottom_part
    for line in full_diamond:
        print(line)

if __name__ == '__main__':
    sample_height = 5
    print_diamond(sample_height)