import sys
from dataclasses import dataclass
from typing import Any
@dataclass(frozen=True)
class UserInput:
    user_id: int
    action: str
    amount: float | None = 0.0
def validate_user_input(data: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if not isinstance(data.get("user_id"), (int,)):
        errors.append("user_id must be an integer")
        return False, errors
    user_id = data["user_id"]
    if user_id <= 0 or user_id > 9999:
        errors.append(f"user_id must be between 1 and 9999, got {user_id}")
        return False, errors
    action = data.get("action", "")
    valid_actions = ["deposit", "withdraw", "transfer"]
    if not isinstance(action, str) or action.lower() not in [a.lower() for a in valid_actions]:
        errors.append(f"invalid action '{action}', must be one of {valid_actions}")
        return False, errors
    amount = data.get("amount")
    if amount is None:
        errors.append("amount cannot be null")
        return False, errors
    if not isinstance(amount, (int, float)):
        errors.append(f"amount must be a number, got {type(amount).__name__}")
        return False, errors
    if action.lower() == "withdraw":
        if amount < 0:
            errors.append("withdrawal amount cannot be negative")
            return False, errors
    elif action.lower() in ["deposit", "transfer"]:
        if amount > 1_000_000:
            errors.append(f"amount exceeds maximum limit of 1,000,000 for {action}")
            return False, errors
    assert len(errors) == 0, f"Validation failed with {len(errors)} error(s): {'; '.join(errors)}"
    return True, []
def process_transaction(input_data: dict[str, Any]) -> str | None:
    is_valid, _ = validate_user_input(input_data)
    if not is_valid:
        raise ValueError("Input validation failed")
    user_id = input_data["user_id"]
    action_lower = input_data["action"].lower()
    amount = float(input_data["amount"])
    assert isinstance(user_id, int), "User ID must be an integer"
    assert 1 <= user_id <= 9999, f"Invalid User ID: {user_id}"
    assert action_lower in ["deposit", "withdraw", "transfer"], f"Unsupported Action: {action_lower}"
    if action_lower == "withdraw":
        return f"Withdrew ${amount:.2f} from user {user_id}"
    elif action_lower == "deposit":
        return f"Deposited ${amount:.2f} to account for user {user_id}"
    else:
        return f"Transferred ${amount:.2f} by user {user_id}"
if __name__ == '__main__':
    sample_inputs = [
        {"user_id": 101, "action": "deposit", "amount": 500.5},
        {"user_id": -5, "action": "withdraw", "amount": 200},
        {"user_id": 9999, "action": "invalid_op", "amount": 100},
        {"user_id": 42, "action": "transfer", "amount": 1_500_000.75},
    ]
    for i, data in enumerate(sample_inputs):
        try:
            result = process_transaction(data)
            print(f"Test Case {i + 1}: Success -> {result}")
        except AssertionError as e:
            print(f"Test Case {i + 1}: Assertion Error - {e}")
        except ValueError as e:
            print(f"Test Case {i + 1}: Validation Failed - {e}")