class BooleanEvaluator:
    def check_complex_condition(self, nested_states: dict) -> bool:
        def evaluate(state):
            if isinstance(state, bool):
                return state
            elif isinstance(state, dict):
                if not state:
                    return False
                return all(evaluate(value) for value in state.values())
            else:
                return bool(state)
        return evaluate(nested_states)
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_data_1 = {
        "A": True,
        "B": False,
        "C": True,
        "D": {
            "E": True,
            "F": False
        }
    }
    sample_data_2 = {
        "X": True,
        "Y": {
            "P": False,
            "Q": True
        },
        "R": False
    }
    print(f"Result for sample_data_1: {evaluator.check_complex_condition(sample_data_1)}")
    print(f"Result for sample_data_2: {evaluator.check_complex_condition(sample_data_2)}")