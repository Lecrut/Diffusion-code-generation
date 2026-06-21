import heapq

def find_minimum(numbers):
    return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [5, 3, 9, 1, 12]
    print(find_minimum(sample_numbers))