class LogicChecker:
    def evaluate(self, bool_list):
        if not bool_list:
            return True
        index = 0
        length = len(bool_list)
        while index < length:
            if not bool_list[index]:
                return False
            index += 1
        return True

if __name__ == '__main__':
    checker = LogicChecker()
    results = []
    results.append(checker.evaluate([True, True, True]))
    results.append(checker.evaluate([True, False, True]))
    results.append(checker.evaluate([]))
    results.append(checker.evaluate([False]))
    results.append(checker.evaluate([True, True]))
    print(results)