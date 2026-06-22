from typing import List

def count_even_numbers(low: int, high: int) -> int:
    count = 0
    for number in range(low, high + 1):
        if number % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    sample_low = 1
    sample_high = 10
    result = count_even_numbers(sample_low, sample_high)
    print(result)