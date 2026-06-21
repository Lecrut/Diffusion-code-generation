class ListSum:
    @staticmethod
    def sum_elements(lst):
        return sum(lst)

if __name__ == '__main__':
    calculator = ListSum()
    sample_list = [1, 2, 3, 4, 5]
    print(calculator.sum_elements(sample_list))
    another_list = [10, 20, 30, 40, 50]
    print(calculator.sum_elements(another_list))