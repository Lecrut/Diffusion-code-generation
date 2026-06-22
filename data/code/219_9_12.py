class MaxFinder:
    def __init__(self, data):
        self.data = data

    def parse_data(self):
        return [int(num) for num in self.data.split(',')]

    def find_max(self):
        parsed_data = self.parse_data()
        if not parsed_data:
            raise ValueError("No numbers found")
        return max(parsed_data)

if __name__ == '__main__':
    finder = MaxFinder("10,5,20,3")
    result = finder.find_max()
    print(result)