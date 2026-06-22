class MinFinder:
    @staticmethod
    def find_min(values):
        if not values:
            raise ValueError("The list is empty")
        min_value = values[0]
        for value in values:
            if value < min_value:
                min_value = value
        return min_value

if __name__ == '__main__':
    data = [3.14, 2.71, 1.618, 0.577, 1.414]
    min_value = MinFinder.find_min(data)
    print(min_value)