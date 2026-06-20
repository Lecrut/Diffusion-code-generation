class OrConditionChecker:
    @staticmethod
    def check_or_conditions(list_of_tuples):
        result = []
        for conditions in list_of_tuples:
            if conditions[0] or conditions[1]:
                result.append(True)
            else:
                result.append(False)
        return result

if __name__ == '__main__':
    sample_data = [
        (True, False),
        (False, False),
        (True, True),
        (False, True),
        (False, False)
    ]
    output = OrConditionChecker.check_or_conditions(sample_data)
    print(output)