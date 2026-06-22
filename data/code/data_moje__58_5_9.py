def count_even_numbers(start, end):
    if start > end:
        return 0
    count = (end // 2) - ((start - 1) // 2)
    return count

if __name__ == '__main__':
    result = count_even_numbers(3, 15)
    print(result)