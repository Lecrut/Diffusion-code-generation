import sys
def sort_numbers(numbers: list) -> None:
    sorted_list = sorted(numbers)
    for i in range(len(sorted_list)):
        print(f"{sorted_list[i]}")
if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    sort_numbers(sample_data)