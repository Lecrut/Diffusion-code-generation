import heapq

def find_largest_value(numbers):
    return heapq.nlargest(1, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [34, 56, 78, 90, 23, 67, 12, 89]
    largest_value = find_largest_value(sample_numbers)
    print(largest_value)