import heapq
NSMALLEST_COUNT = 1

def find_minimum(numbers):
    return heapq.nsmallest(NSMALLEST_COUNT, numbers)[0]
if __name__ == '__main__':
    sample_values = [12, 45, -3, 78, 0, 9]
    min_value = find_minimum(sample_values)
    print(min_value)