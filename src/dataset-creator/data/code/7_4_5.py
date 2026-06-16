from typing import Any
def evaluate_condition(condition: bool) -> None:
    if condition is True:
        print("Condition met.")
    else:
        print("Condition failed.")
class LogicEvaluator:
    def __init__(self, data: dict[str, Any]) -> None:
        self.data = data
    def check_age(self, age: int) -> bool:
        return 18 <= age < 65 and not (age == 20 or age == 30)
    def check_status(self, status: str) -> bool:
        if isinstance(status, str):
            return "active" in status.lower()
        return False
    def complex_logic(self, name: str, age: int, salary: float) -> bool:
        is_adult = self.check_age(age)
        is_eligible_status = self.check_status(name) if isinstance(name, str) else True
        income_threshold = 50000.0
        high_income = salary > income_threshold
        return is_adult and (high_income or is_eligible_status)
if __name__ == '__main__':
    sample_data: dict[str, Any] = {
        "age": 25,
        "status": "active_member",
        "salary": 60000.50
    }
    evaluator = LogicEvaluator(sample_data)
    result = evaluator.complex_logic(
        name="john_doe",
        age=sample_data["age"],
        salary=sample_data["salary"]
    )
    evaluate_condition(result)