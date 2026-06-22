class LogicChecker:
    _TRUE = True
    _FALSE = False

    def evaluate(self, conditions):
        accumulator = LogicChecker._TRUE
        for current_state in conditions:
            if current_state is LogicChecker._FALSE:
                return LogicChecker._FALSE
            accumulator = current_state
        return accumulator

if __name__ == '__main__':
    verifier = LogicChecker()
    group_alpha = [True, True, True]
    group_beta = [True, False, True]
    group_gamma = [False, False]
    group_delta = []
    group_epsilon = [True]

    print(verifier.evaluate(group_alpha))
    print(verifier.evaluate(group_beta))
    print(verifier.evaluate(group_gamma))
    print(verifier.evaluate(group_delta))
    print(verifier.evaluate(group_epsilon))