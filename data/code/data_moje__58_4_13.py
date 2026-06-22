from typing import List

def count_evens(low: int, high: int) -> int:
    count = 0
    for number in range(low, high + 1):
        if number % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    result = count_evens(1, 10)
    print(result)