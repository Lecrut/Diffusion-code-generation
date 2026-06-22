class TruthyChecker:
    def __init__(self, lst):
        self.lst = lst

    def contains_truthy(self):
        return any(self.lst)

if __name__ == '__main__':
    sample_list1 = [0, False, None, '']
    sample_list2 = [0, False, None, 'hello']
    
    checker1 = TruthyChecker(sample_list1)
    checker2 = TruthyChecker(sample_list2)
    
    print(checker1.contains_truthy())
    print(checker2.contains_truthy())