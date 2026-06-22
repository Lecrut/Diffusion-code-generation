from typing import Union

def count_evens(low: int, high: int) -> int:
    count = 0
    for number in range(low, high + 1):
        if number % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    start = 10
    end = 25
    result = count_evens(start, end)
    print(result)