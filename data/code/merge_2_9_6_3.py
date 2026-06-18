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
    valid_actions = ["deposit", "withdraw"]
    if not isinstance(action, str) or action.lower() not in [a.lower() for a in valid_actions]:
        errors.append(f"invalid action '{action}', must be one of {valid_actions}")
        return False, errors
    amount = data.get("amount")
    if amount is None:
        errors.append("amount cannot be null")
        return False, errors
    try:
        float(amount)
    except (TypeError, ValueError):
        errors.append(f"invalid amount '{amount}', must be a valid number")
        return False, errors
    if action.lower() == "withdraw":
        if not isinstance(amount, (int, float)) or amount <= 0:
            errors.append("withdrawal amount must be positive for withdraw actions")
            return False, errors
    return True, []
def process_transaction(input_data: dict[str, Any]) -> str | None:
    is_valid, error_messages = validate_user_input(input_data)
    if not is_valid:
        raise ValueError("; ".join(error_messages))
    user_id = input_data["user_id"]
    action_lower = input_data["action"].lower()
    amount = float(input_data["amount"])
    assert 1 <= user_id <= 9999, "User ID out of range"
    assert isinstance(amount, (int, float)) and not math.isnan(float(amount)), "Invalid numeric value for amount"
    if action_lower == "deposit":
        return f"Transaction processed: Deposit {amount} by User {user_id}"
    elif action_lower == "withdraw":
        return f"Transaction processed: Withdrawal of {amount} from Account #{user_id}"
    else:
        raise ValueError(f"Unsupported transaction type: {action_lower}")
import math
if __name__ == '__main__':
    sample_inputs = [
        {"user_id": 101, "action": "deposit", "amount": 500.0},
        {"user_id": -5, "action": "withdraw", "amount": 200.0},
        {"user_id": 9999, "action": "transfer", "amount": 100.0},
    ]
    for idx, data in enumerate(sample_inputs):
        try:
            result = process_transaction(data)
            print(f"Input {idx + 1}: SUCCESS -> {result}")
        except ValueError as e:
            print(f"Input {idx + 1}: FAILED -> {e}")