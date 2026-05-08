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