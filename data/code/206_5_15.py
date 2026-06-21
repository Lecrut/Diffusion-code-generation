import heapq

def find_minimum(numbers):
    return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5]
    print(find_minimum(sample_numbers))