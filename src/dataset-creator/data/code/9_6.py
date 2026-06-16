import sys
from dataclasses import dataclass
from typing import Any
@dataclass(frozen=True)
class UserInput:
    age: int
    name: str
    balance: float
def validate_age(value: Any) -> bool:
    return isinstance(value, int) and value > 0 and value < 150
def validate_name(value: Any) -> bool:
    if not isinstance(value, str):
        raise ValueError("Name must be a string")
    name = value.strip()
    return len(name) >= 2 and all(c.isalpha() for c in name)
def validate_balance(value: Any) -> bool:
    if not isinstance(value, (int, float)):
        raise TypeError("Balance must be numeric")
    balance = float(value)
    return balance > 0.01
class IntegrityValidator:
    def __init__(self):
        self.errors: list[str] = []
    def validate(self, data: UserInput) -> bool:
        if not validate_age(data.age):
            self.errors.append(f"Invalid age: {data.age}")
            return False
        if not validate_name(data.name):
            self.errors.append(f"Invalid name: {data.name}")
            return False
        if not validate_balance(data.balance):
            self.errors.append(f"Invalid balance: {data.balance}")
            return False
        return True
class RuleProcessor:
    def __init__(self, validator: IntegrityValidator):
        self.validator = validator
    def process(self, data: UserInput) -> str | None:
        if not self.validator.validate(data):
            for error in self.validator.errors:
                print(error)
            return "Validation failed"
        return f"Processed {data.name}, Age: {data.age}, Balance: ${data.balance:.2f}"
if __name__ == '__main__':
    validator = IntegrityValidator()
    processor = RuleProcessor(validator)
    sample_data = UserInput(age=25, name="Alice", balance=100.50)
    result = processor.process(sample_data)
    print(result if result else "No action taken")