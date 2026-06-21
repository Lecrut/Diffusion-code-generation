class ListChecker:
    def __init__(self, master_list):
        self.master_set = set(master_list)

    def check_presence(self, target_list):
        for item in target_list:
            if item in self.master_set:
                return True
        return False

if __name__ == '__main__':
    checker = ListChecker(list(range(1, 100)))
    target = [1, 5, 9, 12]
    result = checker.check_presence(target)
    print(result)