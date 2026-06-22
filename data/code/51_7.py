def right_aligned_pyramid(row_count=8):
    for row in range(1, row_count + 1):
        spaces = ' ' * (row_count - row)
        numbers = ' '.join(str(i) for i in range(1, row + 1))
        yield spaces + numbers

if __name__ == '__main__':
    for line in right_aligned_pyramid(8):
        print(line)