from typing import List

def compute_mean(numbers: List[int]) -> float:
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    if count == 0:
        raise ValueError("List must contain at least one element")
    return total / count

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result = compute_mean(data)
    print(result)