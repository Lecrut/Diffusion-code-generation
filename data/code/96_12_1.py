class BooleanEvaluator:
    def check_complex_condition(self, nested_states: dict) -> bool:
        def evaluate(state):
            if isinstance(state, bool):
                return state
            elif isinstance(state, dict):
                if not state:
                    return False
                return all(evaluate(value) for value in state.values())
            return False
        return evaluate(nested_states)
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample1 = {
        "A": True,
        "B": False,
        "C": True
    }
    result1 = evaluator.check_complex_condition(sample1)
    print(f"Result 1: {result1}")
    sample2 = {
        "X": True,
        "Y": True,
        "Z": False
    }
    result2 = evaluator.check_complex_condition(sample2)
    print(f"Result 2: {result2}")
    sample3 = {
        "P": True,
        "Q": False,
        "R": True,
        "S": True
    }
    result3 = evaluator.check_complex_condition(sample3)
    print(f"Result 3: {result3}")
    sample4 = {
        "Empty": {}
    }
    result4 = evaluator.check_complex_condition(sample4)
    print(f"Result 4: {result4}")
    sample5 = {
        "All": True
    }
    result5 = evaluator.check_complex_condition(sample5)
    print(f"Result 5: {result5}")