class ArrayUtils:
    @staticmethod
    def get_last_element(arr):
        return arr[-1]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    print(ArrayUtils.get_last_element(sample_list))