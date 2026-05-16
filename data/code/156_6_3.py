import sys
def calculate_average_memory_efficient(data):
    if not data:
        return 0
    total = 0
    count = 0
    for x in data:
        total += x
        count += 1
    return total / count
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    average = calculate_average_memory_efficient(sample_list)
    print(average)
    sample_list_empty = []
    average_empty = calculate_average_memory_efficient(sample_list_empty)
    print(average_empty)
    sample_list_floats = [3.5, 7.2, 1.1]
    average_floats = calculate_average_memory_efficient(sample_list_floats)
    print(average_floats)