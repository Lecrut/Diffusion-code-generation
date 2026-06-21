import heapq

def find_min_value(numbers):
    return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 6]
    min_value = find_min_value(sample_numbers)
    print(min_value)