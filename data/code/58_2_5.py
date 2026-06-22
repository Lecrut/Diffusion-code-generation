def count_even_in_range(start: int, end: int) -> int:
    if start > end:
        return 0
    if start & 1:
        start += 1
    if end & 1:
        end -= 1
    if start > end:
        return 0
    return (end - start) >> 1 | 1

if __name__ == '__main__':
    start_value = 10
    end_value = 20
    result = count_even_in_range(start_value, end_value)
    print(result)