class MaxFinder:
    def find_max(self, iterable):
        return max(iterable)
if __name__ == '__main__':
    data = [3, 5, 12, 89, -4]
    result = MaxFinder().find_max(data)
    print(result)