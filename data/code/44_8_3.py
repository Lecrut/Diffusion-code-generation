from typing import List

def compute_mean(numbers: List[int]) -> float:
    if not numbers:
        raise ValueError("List must not be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)