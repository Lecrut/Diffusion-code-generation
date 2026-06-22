def count_even_numbers(low: int, high: int) -> int:
    return sum(1 for num in range(low, high + 1) if num % 2 == 0)

if __name__ == '__main__':
    low = 1
    high = 10
    print(count_even_numbers(low, high))