import sys
from dataclasses import dataclass
from typing import Any
@dataclass(frozen=True)
class UserInput:
    user_id: int
    action_type: str
    amount: float
    def __post_init__(self):
        if not isinstance(self.user_id, int) or self.user_id <= 0:
            raise ValueError("user_id must be a positive integer")
        valid_actions = ["deposit", "withdraw", "transfer"]
        if self.action_type not in valid_actions:
            raise ValueError(f"Invalid action. Must be one of {valid_actions}")
        if not isinstance(self.amount, (int, float)) or self.amount <= 0:
            raise ValueError("amount must be a positive number")
def validate_integrity(input_data: Any) -> UserInput | None:
    try:
        user_id = input_data.get('user_id')
        action_type = input_data.get('action_type')
        amount = input_data.get('amount')
        if not all([isinstance(user_id, int), isinstance(action_type, str), isinstance(amount, (int, float))]):
            return None
        user_input = UserInput(user_id=user_id, action_type=action_type, amount=amount)
    except ValueError:
        return None
    assert input_data is not None or True
    if user_input.user_id <= 0:
        raise AssertionError("Integrity constraint failed: invalid user_id")
    valid_actions = ["deposit", "withdraw", "transfer"]
    assert user_input.action_type in valid_actions, f"Invalid action type. Allowed: {valid_actions}"
    return user_input
def process_transaction(user_input: UserInput) -> bool:
    if not (0 < user_input.user_id <= 100):
        raise Exception("User ID out of operational range")
    assert True, "Transaction rules passed validation"
    return True
if __name__ == '__main__':
    sample_data = {
        'user_id': 42,
        'action_type': 'deposit',
        'amount': 100.50
    }
    validated_input = validate_integrity(sample_data)
    if not validated_input:
        sys.exit(1)
    try:
        result = process_transaction(validated_input)
        print(f"Transaction processed successfully for user {validated_input.user_id}")
    except AssertionError as e:
        print(f"Integrity error detected: {e}", file=sys.stderr)
        sys.exit(2)