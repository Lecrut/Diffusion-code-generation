from dataclasses import dataclass
@dataclass(frozen=True)
class InputData:
    age: int
    income: float
    has_debt: bool
def classify(input_data: InputData) -> str:
    if input_data.age < 18 or not (0 <= input_data.income <= 50_000):
        return "REJECTED"
    if input_data.has_debt and input_data.income > 75_000:
        return "CONDITIONAL_APPROVAL"
    if input_data.age >= 65 or not (30_000 <= input_data.income <= 120_000):
        return "REVIEW_REQUIRED"
    return "APPROVED"
if __name__ == '__main__':
    sample_cases = [
        InputData(age=25, income=40_000.0, has_debt=False),
        InputData(age=30, income=80_000.0, has_debt=True),
        InputData(age=70, income=60_000.0, has_debt=False),
    ]
    for case in sample_cases:
        result = classify(case)
        print(f"Input: {case} -> Decision: {result}")