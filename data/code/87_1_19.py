class ConditionCombiner:
    @staticmethod
    def check_combined_conditions(bool1, bool2):
        return bool1 or bool2

if __name__ == '__main__':
    combiner = ConditionCombiner()
    print(combiner.check_combined_conditions(True, False))
    print(combiner.check_combined_conditions(False, True))
    print(combiner.check_combined_conditions(True, True))
    print(combiner.check_combined_conditions(False, False))