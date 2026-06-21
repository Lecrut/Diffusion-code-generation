import heapq

def find_min_value(numbers):
    return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_data = [8, 3, 5, 7, 2]
    min_value = find_min_value(sample_data)
    print(min_value)