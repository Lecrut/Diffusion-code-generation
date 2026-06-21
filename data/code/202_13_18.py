import heapq

def find_largest_value(numbers):
    return heapq.nlargest(1, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [3, 5, 2, 8, 1, 9, 4]
    largest_value = find_largest_value(sample_numbers)
    print(largest_value)