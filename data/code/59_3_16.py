class ListMiddleFinder:
    @staticmethod
    def find_middle(data):
        return sorted(data)[len(data) // 2]

if __name__ == '__main__':
    sample = [7, 1, 3, 5, 9]
    print(ListMiddleFinder.find_middle(sample))