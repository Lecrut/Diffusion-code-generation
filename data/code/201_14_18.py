from typing import List

def calculate_average(data: List[float]) -> float:
    if not data:
        raise ValueError("Data list cannot be empty")
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    average = calculate_average(sample_data)
    print(f"The average is: {average}")