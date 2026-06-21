import statistics

def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be a list of numbers")

def find_median(data):
    validate_input(data)
    return statistics.median(data)

if __name__ == '__main__':
    sample_list_odd = [1, 5, 3, 7, 9]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [42]
    sample_list_empty = []
    
    print(f"Median of {sample_list_odd}: {find_median(sample_list_odd)}")
    print(f"Median of {sample_list_even}: {find_median(sample_list_even)}")
    print(f"Median of {sample_list_single}: {find_median(sample_list_single)}")
    try:
        print(f"Median of empty list: {find_median(sample_list_empty)}")
    except ValueError as e:
        print(e)