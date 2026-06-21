class SecuritySystemEvaluator:
    HARDWARE_STATUS = 0
    SOFTWARE_INTEGRITY = 1
    NETWORK_CONNECTIVITY = 2

    @staticmethod
    def evaluate_conditions(vars_list, nested_conditions):
        all_true = True
        for condition_set in nested_conditions:
            all_true = all_true and all(vars_list[i] == condition_set[0] for i in range(len(condition_set)))
        return all_true

if __name__ == '__main__':
    variables = [True, False, True]
    conditions = [
        (SecuritySystemEvaluator.HARDWARE_STATUS, True),
        (SecuritySystemEvaluator.SOFTWARE_INTEGRITY, False),
        (SecuritySystemEvaluator.NETWORK_CONNECTIVITY, True)
    ]
    result = SecuritySystemEvaluator.evaluate_conditions(variables, conditions)
    print(result)