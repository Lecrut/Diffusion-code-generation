import heapq
SMALL_NUM = 0.1

def extract_smallest_element(numbers):
    return heapq.nsmallest(1, numbers)[0]
if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 1.9, 5.6]
    smallest_number = extract_smallest_element(sample_numbers)
    print(smallest_number)