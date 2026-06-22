class ListChecker:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_sorted_ascending(self):
        for i in range(len(self.numbers) - 1):
            if self.numbers[i+1] <= self.numbers[i]:
                return False
        return True

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [5, 6, 7, 8, 9]
    sample_list3 = [10, 9, 8, 7]
    sample_list4 = [1, 1, 1, 1]
    
    checker1 = ListChecker(sample_list1)
    checker2 = ListChecker(sample_list2)
    checker3 = ListChecker(sample_list3)
    checker4 = ListChecker(sample_list4)
    
    print(checker1.is_sorted_ascending())
    print(checker2.is_sorted_ascending())
    print(checker3.is_sorted_ascending())
    print(checker4.is_sorted_ascending())