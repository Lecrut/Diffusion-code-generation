class MaxFinder:
    def __init__(self):
        self.max_value = None

    @staticmethod
    def find_max_in_subarray(subarray):
        if not subarray:
            return None
        return max(subarray)

    def update_max(self, value):
        if self.max_value is None or value > self.max_value:
            self.max_value = value

    def find_maximum(self, two_d_array):
        if not two_d_array:
            return None
        for subarray in two_d_array:
            subarray_max = self.find_max_in_subarray(subarray)
            if subarray_max is not None:
                self.update_max(subarray_max)
        return self.max_value

if __name__ == '__main__':
    finder = MaxFinder()
    input_data = [[10, 5, 20], [8, 15], [], [3, 45, 11]]
    result = finder.find_maximum(input_data)
    print(result)