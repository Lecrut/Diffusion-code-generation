class EvenGreaterChecker:
    @staticmethod
    def check(lst):
        flag = False
        for element in lst:
            if element % 2 == 0 and element > 50:
                flag = True
                break
        return flag

if __name__ == '__main__':
    sample_list = [45, 60, 75, 80]
    print(EvenGreaterChecker.check(sample_list))