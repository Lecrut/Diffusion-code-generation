import heapq

class MinFinder:
    MIN_COUNT = 1
    
    @staticmethod
    def find_min(numbers):
        return heapq.nsmallest(MinFinder.MIN_COUNT, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 6]
    min_value = MinFinder.find_min(sample_numbers)
    print(min_value)