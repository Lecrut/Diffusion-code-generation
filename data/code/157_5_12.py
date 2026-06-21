import heapq

def extract_smallest_element(numbers):
    if not numbers:
        raise ValueError("The input list cannot be empty")
    smallest = heapq.nsmallest(1, numbers)
    return smallest[0]

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 1.9, 5.6]
    smallest_number = extract_smallest_element(sample_numbers)
    print(smallest_number)