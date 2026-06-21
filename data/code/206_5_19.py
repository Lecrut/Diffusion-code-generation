import heapq

def find_min_with_heappq(numbers):
    smallest = heapq.nsmallest(1, numbers)
    return smallest[0]

if __name__ == '__main__':
    sample_data = [8, 3, 7, 2, 5]
    min_value = find_min_with_heappq(sample_data)
    print(min_value)