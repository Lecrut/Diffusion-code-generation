class MaxFinder:
    @staticmethod
    def find_maximum(values):
        if not values:
            return None
        max_value = max(values)
        return max_value

if __name__ == '__main__':
    sample_values = [15, 8, 22, 4, 30, 11]
    result = MaxFinder.find_maximum(sample_values)
    print(result)