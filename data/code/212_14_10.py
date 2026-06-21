class MinMaxFinder:
    @staticmethod
    def find_min_max(data):
        if not data:
            return None, None
        minimum = maximum = data[0]
        for element in data:
            if element < minimum:
                minimum = element
            if element > maximum:
                maximum = element
        return minimum, maximum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 100.0, -50.2]
    finder = MinMaxFinder()
    min_val, max_val = finder.find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")