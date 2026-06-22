from enum import Enum
from dataclasses import dataclass
from typing import List

class StatePriority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

@dataclass
class ValidationRule:
    name: str
    condition_func: callable
    priority: StatePriority

@dataclass
class ValidationResult:
    passed: bool
    reason: str
    active_rule: str

class StateValidator:
    def __init__(self):
        self.rules: List[ValidationRule] = []
        self._register_default_rules()

    def _register_default_rules(self):
        self.rules.append(ValidationRule(
            name="critical_override",
            condition_func=lambda a, b, c, d: a and not b,
            priority=StatePriority.HIGH
        ))
        self.rules.append(ValidationRule(
            name="medium_dependency",
            condition_func=lambda a, b, c, d: (not a) and b and c,
            priority=StatePriority.MEDIUM
        ))
        self.rules.append(ValidationRule(
            name="low_condition",
            condition_func=lambda a, b, c, d: (a or b) and (c or d),
            priority=StatePriority.LOW
        ))
        self.rules.append(ValidationRule(
            name="default_fail",
            condition_func=lambda a, b, c, d: False,
            priority=StatePriority.LOW
        ))

    def validate(self, flag_a: bool, flag_b: bool, flag_c: bool, flag_d: bool) -> ValidationResult:
        sorted_rules = sorted(self.rules, key=lambda r: r.priority.value)
        for rule in sorted_rules:
            is_matched = rule.condition_func(flag_a, flag_b, flag_c, flag_d)
            if is_matched:
                passed = self._evaluate_rule_outcome(rule, flag_a, flag_b, flag_c, flag_d)
                return ValidationResult(
                    passed=passed,
                    reason=f"Rule {rule.name} matched",
                    active_rule=rule.name
                )
        return ValidationResult(
            passed=False,
            reason="No rules matched",
            active_rule="none"
        )

    def _evaluate_rule_outcome(self, rule: ValidationRule, a: bool, b: bool, c: bool, d: bool) -> bool:
        if rule.name == "critical_override":
            return a and not b
        elif rule.name == "medium_dependency":
            return (not a) and b and c
        elif rule.name == "low_condition":
            return (a or b) and (c or d)
        return False

if __name__ == '__main__':
    validator = StateValidator()
    test_inputs = [
        (True, False, False, False),
        (False, True, True, False),
        (True, True, True, True),
        (False, False, False, False),
        (True, False, True, False)
    ]
    outcomes = []
    for a, b, c, d in test_inputs:
        result = validator.validate(a, b, c, d)
        outcomes.append(result)
    print(outcomes[0].passed)
    print(outcomes[1].active_rule)
    print(outcomes[2].reason)
    print(outcomes[3].passed)
    print(outcomes[4].passed)