def calculate_average(data):
    total = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
        else:
            raise TypeError("Input contains non-numeric data")
    if not data:
        return 0
    return total / len(data)
if __name__ == '__main__':
    sample_list_valid = [10, 20, 30, 40, 50]
    sample_list_empty = []
    sample_list_mixed = [10, 20, "a", 40]
    sample_tuple_valid = (5.5, 6.5, 7.5)
    print(f"Average of {sample_list_valid}: {calculate_average(sample_list_valid)}")
    print(f"Average of {sample_list_empty}: {calculate_average(sample_list_empty)}")
    try:
        calculate_average(sample_list_mixed)
    except TypeError as e:
        print(f"Error for {sample_list_mixed}: {e}")
    print(f"Average of {sample_tuple_valid}: {calculate_average(sample_tuple_valid)}")