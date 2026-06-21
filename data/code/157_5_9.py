import heapq

def extract_smallest(numbers):
    return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [7.2, 3.4, 5.6, 2.1, 8.9]
    smallest_number = extract_smallest(sample_numbers)
    print(smallest_number)