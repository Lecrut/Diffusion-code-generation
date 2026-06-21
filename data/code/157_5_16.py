import heapq

def find_smallest_element(numbers):
    if not numbers:
        raise ValueError("The input list is empty")
    
    smallest = heapq.nsmallest(1, numbers)[0]
    return smallest

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 1.9, 5.6]
    try:
        smallest_number = find_smallest_element(sample_numbers)
        print(smallest_number)
    except ValueError as e:
        print(e)