class MinValueFinder:
    @staticmethod
    def find_min(values):
        if not values:
            raise ValueError("List is empty")
        return min(values)

if __name__ == '__main__':
    sample_values = [42, 15, 89, 3, 77, 21]
    try:
        result = MinValueFinder.find_min(sample_values)
        print(result)
    except ValueError as e:
        print(e)