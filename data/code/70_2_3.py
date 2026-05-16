class ListChecker:
    def get_extremes(self, data):
        if not data:
            return None
        return (data[0], data[-1])
if __name__ == '__main__':
    checker = ListChecker()
    sample_list = [10, 20, 30, 40, 50]
    result1 = checker.get_extremes(sample_list)
    print(f"List: {sample_list}, Extremes: {result1}")
    sample_list_2 = ['a', 'b', 'c']
    result2 = checker.get_extremes(sample_list_2)
    print(f"List: {sample_list_2}, Extremes: {result2}")
    sample_list_3 = [99]
    result3 = checker.get_extremes(sample_list_3)
    print(f"List: {sample_list_3}, Extremes: {result3}")
    sample_list_4 = []
    result4 = checker.get_extremes(sample_list_4)
    print(f"List: {sample_list_4}, Extremes: {result4}")