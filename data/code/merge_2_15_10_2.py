import sys
def sort_numbers(numbers: list) -> list:
    return sorted(numbers)
if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 98]
    result = sort_numbers(sample_data)
    print(result)