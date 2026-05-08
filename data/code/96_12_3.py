class BooleanEvaluator:
    def check_complex_condition(self, states: dict) -> bool:
        if not states:
            return False
        def evaluate_nested(sub_states: dict) -> bool:
            if not sub_states:
                return False
            results = []
            for key, value in sub_states.items():
                if isinstance(value, dict):
                    results.append(evaluate_nested(value))
                elif isinstance(value, bool):
                    results.append(value)
                else:
                    results.append(bool(value))
            return all(results)
        return evaluate_nested(states)
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_states_1 = {
        "A": True,
        "B": False,
        "C": {
            "D": True,
            "E": False
        }
    }
    sample_states_2 = {
        "X": True,
        "Y": {
            "P": False,
            "Q": {
                "R": True
            }
        }
    }
    sample_states_3 = {
        "S1": True,
        "S2": False,
        "S3": {
            "S3a": True,
            "S3b": True
        }
    }
    print(f"Result for sample_states_1: {evaluator.check_complex_condition(sample_states_1)}")
    print(f"Result for sample_states_2: {evaluator.check_complex_condition(sample_states_2)}")
    print(f"Result for sample_states_3: {evaluator.check_complex_condition(sample_states_3)}")