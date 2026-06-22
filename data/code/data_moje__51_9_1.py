def build_symmetric_pyramid(rows: int) -> list[str]:
    result = []
    for i in range(1, rows + 1):
        num = i
        left_half = []
        curr = 1
        while curr <= num:
            left_half.append(str(curr))
            curr += 1
        right_half = left_half[-2::-1] if num > 1 else []
        row_nums = left_half + right_half
        row_str = ' '.join(row_nums)
        total_chars = len(row_str)
        padding = (total_chars - len(row_str)) // 2 
        space_padding = ' ' * (rows - i)
        line = space_padding + row_str
        result.append(line)
    return result

def main() -> None:
    pyramid_rows = 6
    lines = build_symmetric_pyramid(pyramid_rows)
    print('\n'.join(lines))
    print(len(lines))
    print(lines[-1])

if __name__ == '__main__':
    main()