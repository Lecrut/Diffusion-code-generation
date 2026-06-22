class MiddleElementFinder:
    _ODD_OFFSET = 0
    _EVEN_OFFSET = -1

    @staticmethod
    def _calculate_index(total_count):
        half = total_count // 2
        if total_count % 2 == 0:
            return half + MiddleElementFinder._EVEN_OFFSET
        return half + MiddleElementFinder._ODD_OFFSET

    @classmethod
    def get_middle(cls, data_source):
        data_list = list(data_source)
        total = len(data_list)
        if total == 0:
            raise ValueError("Cannot find middle element of an empty iterable")
        index = cls._calculate_index(total)
        return data_list[index]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [100, 200, 300, 400]
    single_list = [42]
    
    print(MiddleElementFinder.get_middle(odd_list))
    print(MiddleElementFinder.get_middle(even_list))
    print(MiddleElementFinder.get_middle(single_list))