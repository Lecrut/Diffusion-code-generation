class MaxFinder:
    def find_maximum(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        maximum = data[0]
        for item in data[1:]:
            if item > maximum:
                maximum = item
        return maximum

if __name__ == '__main__':
    finder = MaxFinder()
    sample_values1 = [1, 5, 2, 8, 3]
    sample_values2 = [-10, -5, -20, -1]
    sample_values3 = [42]
    empty_list = []
    print(f"Maximum of {sample_values1}: {finder.find_maximum(sample_values1)}")
    print(f"Maximum of {sample_values2}: {finder.find_maximum(sample_values2)}")
    print(f"Maximum of {sample_values3}: {finder.find_maximum(sample_values3)}")
    try:
        finder.find_maximum(empty_list)
    except ValueError as e:
        print(e)