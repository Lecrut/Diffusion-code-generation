class MaxFinder:
    @staticmethod
    def find_max_value(mixed_list):
        return max(mixed_list)

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, 8.9, 1]
    print(MaxFinder.find_max_value(sample_values))