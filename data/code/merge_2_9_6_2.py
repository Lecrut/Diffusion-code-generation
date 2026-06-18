import sys
from dataclasses import dataclass
from typing import Any
@dataclass(frozen=True)
class UserInput:
    user_id: int
    age: int
    balance: float
    is_verified: bool
def validate_user_input(data: dict[str, Any]) -> tuple[UserInput | None, list[str]]:
    errors = []
    if not isinstance(data.get("user_id"), int) or data["user_id"] <= 0:
        errors.append("user_id must be a positive integer")
    elif len(str(data["user_id"])) > 18:
        errors.append("user_id exceeds maximum length of 18 digits")
    if not isinstance(data.get("age"), int) or data["age"] < 0 or data["age"] > 120:
        errors.append("age must be an integer between 0 and 120")
    if not isinstance(data.get("balance"), (int, float)) or data["balance"] <= 0:
        errors.append("balance must be a positive number")
    if not isinstance(data.get("is_verified"), bool):
        errors.append("is_verified must be a boolean value")
    if len(errors) > 0:
        return None, errors
    user_id = data["user_id"]
    age = data["age"]
    balance = float(data["balance"])
    is_verified = data["is_verified"]
    if is_verified and (age < 18):
        errors.append("Verified user must be at least 18 years old")
        return None, errors
    assert isinstance(user_id, int), "user_id type assertion failed"
    assert isinstance(age, int), "age type assertion failed"
    assert isinstance(balance, float), "balance type assertion failed"
    assert isinstance(is_verified, bool), "is_verified type assertion failed"
    assert user_id > 0 and age >= 0 and balance > 0, "Input values must be positive or non-negative as per constraints"
    return UserInput(user_id=user_id, age=age, balance=balance, is_verified=is_verified), []
if __name__ == '__main__':
    sample_data = {
        "user_id": 123456789012345678,
        "age": 25,
        "balance": 500.50,
        "is_verified": True
    }
    validated_input, validation_errors = validate_user_input(sample_data)
    if not validated_input:
        print("Validation failed:")
        for error in validation_errors:
            print(f" - {error}")
        sys.exit(1)
    assert isinstance(validated_input, UserInput), "Final output must be a UserInput instance"
    if not validated_input.is_verified and (validated_input.balance < 100):
        print("Rule applied: Unverified user with low balance denied access.")
    else:
        print(f"Rule passed for User {validated_input.user_id}.")