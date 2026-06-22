def count_even_numbers(min_val, max_val):
    if min_val > max_val:
        return 0
    if max_val % 2 == 0:
        max_val -= 1
    if min_val % 2 == 0:
        min_val += 1
    if min_val > max_val:
        return 0
    return (max_val - min_val) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(3, 9)
    print(result)