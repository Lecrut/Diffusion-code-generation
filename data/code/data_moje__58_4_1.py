from typing import Optional

def count_even_numbers(low: int, high: int) -> int:
    if low > high:
        return 0
    start = low if low % 2 == 0 else low + 1
    if start > high:
        return 0
    end = high if high % 2 == 0 else high - 1
    return (end - start) // 2 + 1

if __name__ == '__main__':
    sample_low: int = 3
    sample_high: int = 10
    result: int = count_even_numbers(sample_low, sample_high)
    print(result)