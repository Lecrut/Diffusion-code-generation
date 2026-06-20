class ConditionCombiner:
    def check_combined_conditions(self, bool1, bool2):
        return bool1 or bool2

if __name__ == '__main__':
    combiner = ConditionCombiner()
    result1 = combiner.check_combined_conditions(True, False)
    print(f"check_combined_conditions(True, False): {result1}")
    result2 = combiner.check_combined_conditions(False, True)
    print(f"check_combined_conditions(False, True): {result2}")
    result3 = combiner.check_combined_conditions(True, True)
    print(f"check_combined_conditions(True, True): {result3}")
    result4 = combiner.check_combined_conditions(False, False)
    print(f"check_combined_conditions(False, False): {result4}")