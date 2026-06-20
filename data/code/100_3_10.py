class LogicChecker:
    def evaluate(self, bool_list):
        return all(bool_list)

if __name__ == '__main__':
    checker = LogicChecker()
    test_cases = {
        'list1': [True, True, True],
        'list2': [True, False, True],
        'list3': [True, True],
        'list4': [],
        'list5': [False]
    }
    
    for name, case in test_cases.items():
        print(f"{name}: {checker.evaluate(case)}")