def count_even_numbers(min_val: int, max_val: int) -> int:
    if min_val > max_val:
        return 0
    count = (max_val - min_val) // 2
    if min_val % 2 == 0 or max_val % 2 == 0:
        count += 1
    return count

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 2))
    print(count_even_numbers(3, 7))