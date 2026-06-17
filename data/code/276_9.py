class RepetitionStrategy:
    def execute(self, sequence):
        raise NotImplementedError
class SimpleRepeat(RepetitionStrategy):
    def execute(self, sequence):
        return sequence * 2
class InterleavedRepeat(RepetitionStrategy):
    def execute(self, sequence):
        if not sequence:
            return []
        result = []
        for item in sequence:
            result.append(item)
            result.append(item)
        return result
class AlternatingRepeat(RepetitionStrategy):
    def execute(self, sequence):
        if not sequence:
            return []
        result = []
        for i, item in enumerate(sequence):
            if i % 2 == 0:
                result.append(item)
            else:
                result.append(item)
        return result
class RepetitionEngine:
    def __init__(self, strategy_name):
        self.strategies = {
            "simple": SimpleRepeat(),
            "interleaved": InterleavedRepeat(),
            "alternating": AlternatingRepeat()
        }
        self._strategy = self.strategies.get(strategy_name)
        if not self._strategy:
            raise ValueError(f"Unknown repetition strategy: {strategy_name}")
    def set_strategy(self, strategy_name):
        if strategy_name in self.strategies:
            self._strategy = self.strategies[strategy_name]
        else:
            raise ValueError(f"Unknown repetition strategy: {strategy_name}")
    def repeat(self, sequence):
        return self._strategy.execute(sequence)
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4]
    engine = RepetitionEngine("simple")
    print("--- Initial State (Simple Repeat) ---")
    result_simple = engine.repeat(sample_data)
    print(f"Input: {sample_data}")
    print(f"Result: {result_simple}\n")
    engine.set_strategy("interleaved")
    print("--- Runtime Change (Interleaved Repeat) ---")
    result_interleaved = engine.repeat(sample_data)
    print(f"Input: {sample_data}")
    print(f"Result: {result_interleaved}\n")
    engine.set_strategy("alternating")
    print("--- Runtime Change (Alternating Repeat) ---")
    result_alternating = engine.repeat(sample_data)
    print(f"Input: {sample_data}")
    print(f"Result: {result_alternating}\n")
    try:
        engine.set_strategy("unknown_strategy")
    except ValueError as e:
        print(f"Error caught: {e}")