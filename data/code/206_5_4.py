import heapq

def find_min(numbers):
    return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [5, 3, 8, 1, 2]
    print(find_min(sample_numbers))