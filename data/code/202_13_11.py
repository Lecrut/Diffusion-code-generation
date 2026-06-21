import heapq

class MaxFinder:
    def find_largest(self, numbers):
        if not numbers:
            raise ValueError("Input iterable cannot be empty")
        return heapq.nlargest(1, numbers)[0]

if __name__ == '__main__':
    finder = MaxFinder()
    
    list1 = [3, 1, 9, 4, 7]
    print(f"Max of {list1}: {finder.find_largest(list1)}")
    
    tuple2 = (100, 50, 200, 10)
    print(f"Max of {tuple2}: {finder.find_largest(tuple2)}")
    
    list3 = [-5, -1, -10]
    print(f"Max of {list3}: {finder.find_largest(list3)}")