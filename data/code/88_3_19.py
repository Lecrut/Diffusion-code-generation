CONDITION_MET = True
CONDITION_NOT_MET = False

def check_conditions_met(a: bool, b: bool) -> bool:
    return a and b
if __name__ == '__main__':
    sample_cases = [(True, True), (False, True), (True, False), (False, False)]
    for case in sample_cases:
        result = check_conditions_met(*case)
        print(f'Input: {case}, Result: {('Both conditions met' if result else 'At least one condition not met')}')