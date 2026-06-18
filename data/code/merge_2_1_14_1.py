from typing import Any
class DynamicConditionChecker:
    def __init__(self) -> None:
        self._conditions: dict[str, callable] = {}
    def register_condition(self, name: str, check_func: callable) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Condition name must be a non-empty string.")
        self._conditions[name] = check_func
    def evaluate(self, value: Any, condition_name: str | None = None) -> bool:
        results = []
        for cond_name in [condition_name] if condition_name else self._conditions.keys():
            if cond_name not in self._conditions:
                continue
            try:
                result = self._conditions[cond_name](value)
                results.append(result)
            except Exception:                                
                results.append(False)
        return any(results)
if __name__ == '__main__':
    checker = DynamicConditionChecker()
    def is_positive(x: int | float) -> bool:
        return x > 0
    def is_even_int(x: Any) -> bool:
        return isinstance(x, int) and x % 2 == 0
    checker.register_condition("positive", is_positive)
    checker.register_condition("even_integer", is_even_int)
    test_values = [5, -3.7, "10", True]
    for val in test_values:
        result_all = checker.evaluate(val)
        result_specific_1 = checker.evaluate(val, condition_name="positive")
        result_specific_2 = checker.evaluate(val, condition_name="even_integer")
        print(f"Value {val!r}: All={result_all}, Positive={result_specific_1}, EvenInt={result_specific_2}")