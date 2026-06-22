class DifferenceGenerator:
    def __init__(self, data):
        self.data = data

    def generate_differences(self):
        for i in range(len(self.data) - 1):
            yield abs(self.data[i+1] - self.data[i])

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    diff_gen = DifferenceGenerator(sample_list)
    
    for diff in diff_gen.generate_differences():
        print(diff)