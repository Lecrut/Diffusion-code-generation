import heapq

def find_smallest_element(numbers):
    return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9, 5.6]
    smallest_value = find_smallest_element(sample_values)
    print(smallest_value)