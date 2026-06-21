class ZeroChecker:
    @staticmethod
    def contains_zero(numbers):
        return 0 in numbers

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = ZeroChecker.contains_zero(sample_list)
    print(result)

    another_sample_list = [-5, -10, 0, 15]
    print(ZeroChecker.contains_zero(another_sample_list))