def validate_input(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) != 3:
        raise ValueError("List must contain exactly three elements")

def find_median(data):
    validate_input(data)
    sorted_data = sorted(data)
    return sorted_data[1]

if __name__ == '__main__':
    sample_list = [2, 3, 1]
    print(f"Median of {sample_list}: {find_median(sample_list)}")