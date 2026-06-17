class MaxFinder:
    def find_max(self, iterable):
        return max(iterable)
if __name__ == '__main__':
    data = [3, 7, 2, 9, 1]
    result = MaxFinder().find_max(data)
    print(result)