class MinValueFinder:
    @staticmethod
    def find_min(lst):
        return min(lst) if lst else None

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5]
    sample2 = [7]
    sample3 = []
    
    finder = MinValueFinder()
    print(f"Minimum in {sample1}: {finder.find_min(sample1)}")
    print(f"Minimum in {sample2}: {finder.find_min(sample2)}")
    print(f"Minimum in {sample3}: {finder.find_min(sample3)}")