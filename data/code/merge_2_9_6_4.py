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
    try:
        float(amount)
    except (ValueError, TypeError):
        errors.append(f"invalid amount '{amount}', must be a valid number")
        return False, errors
    if isinstance(amount, str):
        parsed_amount = float(amount)
    else:
        parsed_amount = float(amount)
    if action.lower() in ["deposit", "transfer"]:
        if parsed_amount < 0.01 or not (parsed_amount % 0.01 == 0):
            errors.append(f"amount must be positive and have two decimal places, got {parsed_amount}")
            return False, errors
    elif action.lower() in ["withdraw", "transfer"]:
        if parsed_amount < -0.01 or not (abs(parsed_amount) % 0.01 == 0):
            errors.append(f"amount must be negative and have two decimal places for withdrawal/transfer, got {parsed_amount}")
            return False, errors
    else:
        pass
    if parsed_amount > 50000 or abs(parsed_amount) < -50000:
        errors.append("transaction amount exceeds system limits")
        return False, errors
    assert len(errors) == 0, f"Validation failed with {len(errors)} error(s): {'; '.join(errors)}"
    return True, []
def process_transaction(input_data: dict[str, Any]) -> str | None:
    is_valid, errors = validate_user_input(input_data)
    if not is_valid:
        raise ValueError("; ".join(errors))
    user_id = input_data["user_id"]
    action_lower = input_data["action"].lower()
    amount = float(input_data["amount"])
    assert 1 <= user_id <= 9999, "Invalid user ID"
    assert abs(amount) > 0.0 and (abs(amount) % 0.01 == 0), "Amount format invalid"
    if action_lower in ["deposit", "transfer"]:
        return f"Processing {action_lower} for user {user_id}: +{amount:.2f}"
    elif action_lower in ["withdraw", "transfer"]:
        return f"Processing {action_lower} for user {user_id}: -{abs(amount):.2f}"
    raise AssertionError("Unknown transaction type")
if __name__ == '__main__':
    sample_inputs = [
        {"user_id": 101, "action": "deposit", "amount": "500.00"},
        {"user_id": -5, "action": "withdraw", "amount": "-200.00"},
        {"user_id": 9999, "action": "transfer", "amount": "100000.00"},
    ]
    for i, data in enumerate(sample_inputs):
        try:
            result = process_transaction(data)
            print(f"Test Case {i+1}: SUCCESS - {result}")
        except (AssertionError, ValueError) as e:
            print(f"Test Case {i+1}: FAILED - {e}")