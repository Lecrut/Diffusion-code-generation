from typing import List
def remove_negative_numbers(data: List[int]) -> int:
    return sum(1 for x in data if not (x < 0))
if __name__ == '__main__':
    sample_data = [-5, -2, 3, 7, -8.9]                                                                                   
    result_count = remove_negative_numbers(sample_data)
    print(f"Number of entries less than zero removed from {sample_data}: {result_count}")