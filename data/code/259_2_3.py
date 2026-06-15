class MinMaxFinder:
    def get_min_max(self, data_list):
        if not data_list:
            return None, None
        minimum = data_list[0]
        maximum = data_list[0]
        for item in data_list:
            if item < minimum:
                minimum = item
            if item > maximum:
                maximum = item
        return minimum, maximum
if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_data1 = [10, 5, 20, 8, 15]
    min1, max1 = finder.get_min_max(sample_data1)
    print(f"Data: {sample_data1}, Minimum: {min1}, Maximum: {max1}")
    sample_data2 = [-5, 100, 0, -50]
    min2, max2 = finder.get_min_max(sample_data2)
    print(f"Data: {sample_data2}, Minimum: {min2}, Maximum: {max2}")
    sample_data3 = [7]
    min3, max3 = finder.get_min_max(sample_data3)
    print(f"Data: {sample_data3}, Minimum: {min3}, Maximum: {max3}")
    sample_data4 = []
    min4, max4 = finder.get_min_max(sample_data4)
    print(f"Data: {sample_data4}, Minimum: {min4}, Maximum: {max4}")