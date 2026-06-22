class MaxFinder:
    @staticmethod
    def find_max_element(data):
        max_val = data[0]
        for value in data:
            if value > max_val:
                max_val = value
        return max_val

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    print(MaxFinder.find_max_element(sample_data))