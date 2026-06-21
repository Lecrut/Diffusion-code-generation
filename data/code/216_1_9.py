class MedianFinder:
    @staticmethod
    def find_middle(data):
        n = len(data)
        if n == 0:
            raise ValueError("The list is empty")
        middle_index = n // 2
        return data[middle_index]

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    print(MedianFinder.find_middle(sample_list))