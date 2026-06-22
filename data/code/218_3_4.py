class MinStringFinder:
    def __init__(self, data):
        self.data = data
    
    def get_minimum(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        return min(self.data)

if __name__ == '__main__':
    sample_list = ['cherry', 'banana', 'apple']
    finder = MinStringFinder(sample_list)
    minimum_value = finder.get_minimum()
    print(minimum_value)