def build_number_list(start: int, end: int) -> list:
    numbers = []
    for i in range(start, end + 1):
        numbers.append(i)
    return numbers

if __name__ == '__main__':
    sample_start = 2
    sample_end = 8
    result = build_number_list(sample_start, sample_end)
    print(result)