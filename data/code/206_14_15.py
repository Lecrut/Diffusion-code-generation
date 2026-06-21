min_value = lambda lst: min(lst) if lst else None

class MinFinder:
    def find_min(self, lst):
        return min_value(lst)

if __name__ == '__main__':
    finder = MinFinder()
    sample1 = [3, 1, 4, 1, 5]
    sample2 = [7]
    sample3 = []
    
    print(f"Minimum in {sample1}: {finder.find_min(sample1)}")
    print(f"Minimum in {sample2}: {finder.find_min(sample2)}")
    print(f"Minimum in {sample3}: {finder.find_min(sample3)}")