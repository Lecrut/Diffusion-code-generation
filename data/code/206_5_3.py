import heapq

def find_minimum(numbers):
    return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_values = [12, 45, -3, 78, 0, 9]
    min_value = find_minimum(sample_values)
    print(min_value)