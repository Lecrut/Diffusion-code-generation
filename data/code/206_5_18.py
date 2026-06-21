import heapq

MIN_THRESHOLD = 1

def find_min(numbers):
    return heapq.nsmallest(MIN_THRESHOLD, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 6]
    print(find_min(sample_numbers))