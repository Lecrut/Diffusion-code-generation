def calculate_average(data):
    if not data:
        return 0
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(calculate_average(sample_list))
    sample_list_empty = []
    print(calculate_average(sample_list_empty))
    sample_list_floats = [1.5, 2.5, 3.0]
    print(calculate_average(sample_list_floats))