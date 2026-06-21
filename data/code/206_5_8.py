import heapq

def find_min(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 6]
    try:
        print(find_min(sample_numbers))
    except ValueError as e:
        print(e)