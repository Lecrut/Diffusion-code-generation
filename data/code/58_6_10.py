def count_even_numbers(min_val: int, max_val: int) -> int:
    if min_val > max_val:
        return 0

    def count_evens_up_to(n):
        if n < 0:
            return -(-n // 2)
        return n // 2 + 1
    result = count_evens_up_to(max_val) - count_evens_up_to(min_val - 1)
    return result
if __name__ == '__main__':
    min_val = 2
    max_val = 10
    result = count_even_numbers(min_val, max_val)
    print(result)