class MiddleFinder:
    def find_middle(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n == 0:
            return None
        elif n % 2 == 1:
            return sorted_data[n // 2]

if __name__ == '__main__':
    finder = MiddleFinder()
    sample1 = [3, 1, 4, 1, 5]
    print(f"Data: {sample1}, Middle: {finder.find_middle(sample1)}")
    sample2 = [9, 8, 7, 6, 5, 4, 3]
    print(f"Data: {sample2}, Middle: {finder.find_middle(sample2)}")