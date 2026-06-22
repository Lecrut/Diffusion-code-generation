def count_evens(start, end):
    if start > end:
        return 0
    start_even_count = 1 if start % 2 == 0 else 0
    end_even_count = 1 if end % 2 == 0 else 0
    total_numbers = end - start + 1
    num_odds = total_numbers // 2
    if total_numbers % 2 == 1:
        if start % 2 != 0:
            num_odds += 1
    num_evens = total_numbers - num_odds
    return num_evens

if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 2))
    print(count_evens(3, 5))
    print(count_evens(0, 0))
    print(count_evens(-5, 5))