import heapq

class MinFinder:
    @staticmethod
    def find_min(numbers):
        return heapq.nsmallest(1, numbers)[0]

if __name__ == '__main__':
    sample_numbers = [8, 3, 5, 7, 2]
    min_value = MinFinder.find_min(sample_numbers)
    print(min_value)