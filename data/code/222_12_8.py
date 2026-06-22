class MinFinder:
    @staticmethod
    def find_min(data):
        return min(data)

if __name__ == '__main__':
    data = [3, 1, 4, 1, 5, 9, 2]
    min_value = MinFinder.find_min(data)
    print(min_value)