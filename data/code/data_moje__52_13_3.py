def print_diamond_pattern(height: int) -> str:
    if height < 1 or height % 2 == 0:
        return ""
    mid = height // 2
    upper_rows = [
        " " * (mid - i) + "*" * (2 * i + 1)
        for i in range(mid + 1)
    ]
    lower_rows = upper_rows[:-1][::-1]
    all_rows = upper_rows + lower_rows
    return "\n".join(all_rows)

if __name__ == '__main__':
    sample_height = 7
    print(print_diamond_pattern(sample_height))