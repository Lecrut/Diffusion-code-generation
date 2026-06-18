def diff_length_len(a: int, b: int) -> int:
    """Return the length of the difference (absolute value)."""
    return abs(int(a) - int(b))

if __name__ == '__main__':
    # Hard-coded sample values ensuring no external input or files.
    val1 = 10
    val2 = 4
    result = diff_length_len(val1, val2)
    print(result)