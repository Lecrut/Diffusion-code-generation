class MiddleFinder:
    def find_middle(self, data):
        if len(data) % 2 == 0:
            raise ValueError("List must have an odd length.")
        return sorted(data)[len(data) // 2]

if __name__ == '__main__':
    finder = MiddleFinder()
    sample1 = [3, 1, 4, 5, 9]
    print(f"Data: {sample1}, Middle: {finder.find_middle(sample1)}")
    sample2 = [7, 2, 8, 6, 0]
    print(f"Data: {sample2}, Middle: {finder.find_middle(sample2)}")