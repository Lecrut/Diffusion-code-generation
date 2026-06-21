import statistics

def calculate_median(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_list_odd = [1, 5, 3, 7, 9]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [42]
    sample_list_empty = []

    try:
        print(f"Median of {sample_list_odd}: {calculate_median(sample_list_odd)}")
        print(f"Median of {sample_list_even}: {calculate_median(sample_list_even)}")
        print(f"Median of {sample_list_single}: {calculate_median(sample_list_single)}")
        calculate_median(sample_list_empty)
    except ValueError as e:
        print(e)