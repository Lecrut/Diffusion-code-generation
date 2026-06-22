class MaxFinder:
    @staticmethod
    def find_max(data):
        max_element = data[0]
        for number in data:
            if number > max_element:
                max_element = number
        return max_element

if __name__ == '__main__':
    sample_list = [10.5, 7.3, 20.1, 8.9, 15.6]
    result = MaxFinder.find_max(sample_list)
    print(result)