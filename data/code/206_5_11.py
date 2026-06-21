import heapq

def validate_input(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

def find_min_using_heapq(numbers):
    validate_input(numbers)
    return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 6]
    print(find_min_using_heapq(sample_numbers))