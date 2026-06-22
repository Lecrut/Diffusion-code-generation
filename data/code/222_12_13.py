class MinFinder:
    @staticmethod
    def find_min(data):
        if not data:
            raise ValueError("Data list cannot be empty")
        min_value = data[0]
        for item in data[1:]:
            if item < min_value:
                min_value = item
        return min_value

if __name__ == '__main__':
    data = [3.14, 2.71, 1.618, 0.577, 0.367]
    min_value = MinFinder.find_min(data)
    print(min_value)