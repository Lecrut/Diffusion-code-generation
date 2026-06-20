class StrictBooleanEvaluator:
    @staticmethod
    def are_strictly_true(var1, var2):
        return bool(var1) and bool(var2)

if __name__ == '__main__':
    condition_x = True
    condition_y = False
    result = StrictBooleanEvaluator.are_strictly_true(condition_x, condition_y)
    print(result)