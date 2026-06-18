import sys
from dataclasses import dataclass
from typing import Any
@dataclass(frozen=True)
class UserInput:
    user_id: str
    action: str
    amount: float | None = None
def validate_user_input(data: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if not isinstance(data.get("user_id"), str) or len(data["user_id"]) < 3:
        errors.append("Invalid user_id format")
    valid_actions = ["deposit", "withdraw", "transfer"]
    action = data.get("action")
    if action is None or action.lower() not in [a.lower() for a in valid_actions]:
        errors.append(f"Action '{action}' must be one of: {', '.join(valid_actions)}")
    amount_key = "amount" if isinstance(data, dict) else data.get("amount", 0)
    try:
        val_amount = float(amount_key)
        if not (val_amount > 0):
            errors.append("Amount must be a positive number")
    except (ValueError, TypeError):
        errors.append(f"Invalid amount type or value: {type(val_amount)}")
    return len(errors) == 0, errors
def assert_integrity(data: dict[str, Any]) -> None:
    is_valid, error_list = validate_user_input(data)
    if not is_valid:
        for err in error_list:
            raise AssertionError(f"Integrity constraint violated: {err}")
    user_id = data["user_id"]
    action = data.get("action", "").lower()
    assert isinstance(user_id, str), "User ID must be a string"
    if action == "withdraw":
        amount = float(data.get("amount"))
        assert 0 < amount <= 10000.0, f"Withdrawal {amount} exceeds maximum limit of $10,000 or is non-positive"
def process_decision(input_data: dict[str, Any]) -> str:
    try:
        assert_integrity(input_data)
        user_id = input_data["user_id"]
        action = input_data.get("action", "").lower()
        amount = float(input_data.get("amount")) if "amount" in input_data else 0.0
        status_msg = f"{user_id}: {action} initiated successfully."
        return status_msg
    except AssertionError as e:
        raise Exception(f"Decision blocked due to validation failure: {e}")
if __name__ == '__main__':
    sample_inputs = [
        {"user_id": "U12345", "action": "deposit"},
        {"user_id": "A", "action": "withdraw", "amount": 50.0},
        {"user_id": "B98765", "action": "transfer", "amount": -10.0},
    ]
    for i, data in enumerate(sample_inputs):
        try:
            result = process_decision(data)
            print(f"Test Case {i+1}: PASSED -> {result}")
        except Exception as e:
            print(f"Test Case {i+1}: FAILED (Expected Assertion Error) -> {e}")