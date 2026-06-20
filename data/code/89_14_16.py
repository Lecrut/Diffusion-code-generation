class BooleanOperations:

    @staticmethod
    def and_operation(state1, state2):
        return state1 and state2
if __name__ == '__main__':
    state1 = True
    state2 = False
    result = BooleanOperations.and_operation(state1, state2)
    print(result)