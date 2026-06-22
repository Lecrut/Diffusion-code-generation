class AbsoluteDifferenceGenerator:
    def __init__(self, data):
        self.data = data

    def generate_differences(self):
        for i in range(1, len(self.data)):
            yield abs(self.data[i] - self.data[i - 1])

if __name__ == '__main__':
    sample_list = [7, 3, 9, 2, 5]
    diff_generator = AbsoluteDifferenceGenerator(sample_list)
    
    for diff in diff_generator.generate_differences():
        print(diff)