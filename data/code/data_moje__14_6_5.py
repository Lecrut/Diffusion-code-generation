class NegativeIndexHelper:
    THIRD_OFFSET = -3

    @staticmethod
    def get_third_element(arr):
        return arr[NegativeIndexHelper.THIRD_OFFSET]

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25]
    result = NegativeIndexHelper.get_third_element(sample_data)
    print(result)