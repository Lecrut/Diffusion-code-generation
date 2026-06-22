class SafeList:
    DEFAULT_VALUE = None

    @staticmethod
    def safe_access(lst, index):
        return lst[index] if len(lst) > index else SafeList.DEFAULT_VALUE

if __name__ == '__main__':
    sample_list_1 = [100, 200, 300]
    sample_list_2 = [45]
    sample_list_3 = []
    print(SafeList.safe_access(sample_list_1, 1))
    print(SafeList.safe_access(sample_list_2, 1))
    print(SafeList.safe_access(sample_list_3, 1))