import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Callable
from dataclasses import dataclass
from enum import Enum
class RuleType(Enum):
    CONDITION = "condition"
    ACTION = "action"
@dataclass(frozen=True)
class DecisionRule:
    rule_id: str
    rule_type: RuleType
    payload: Dict[str, Any]
    def matches(self, context: Dict[str, Any]) -> bool:
        for key, value in self.payload.items():
            if isinstance(value, list):
                return any(context.get(key) == item for item in value)
            elif callable(value):
                result = value()
                return (context.get(key) is None and not result) or context.get(key) != result
            else:
                return context.get(key) == value
class DecisionEngine:
    def __init__(self, config_path: str, log_level: int = logging.DEBUG):
        self.rules: List[DecisionRule] = []
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        if Path(config_path).exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
            for item in config_data.get('rules', []):
                rule_type_map = {RuleType.CONDITION.value: RuleType.CONDITION, 
                                RuleType.ACTION.value: RuleType.ACTION}
                if 'type' not in item or item['type'] not in rule_type_map:
                    self.logger.error(f"Invalid rule type for ID '{item.get('rule_id')}'. Skipping.")
                    continue
                try:
                    payload = json.loads(item.get('payload', '{}'))
                    decision_rule = DecisionRule(
                        rule_id=item['rule_id'],
                        rule_type=rule_type_map[item['type']],
                        payload=payload
                    )
                    self.rules.append(decision_rule)
                    self.logger.info(f"Loaded rule: {decision_rule.rule_id}")
                except json.JSONDecodeError as e:
                    self.logger.error(f"JSON decode error for ID '{item.get('rule_id')}': {e}")
    def evaluate(self, context: Dict[str, Any]) -> List[DecisionRule]:
        matched_rules = []
        if not self.rules:
            return matched_rules
        sorted_rules = sorted(self.rules, key=lambda r: r.rule_id)
        for rule in sorted_rules:
            try:
                is_match = False
                if rule.rule_type == RuleType.CONDITION and not isinstance(rule.payload.get('action'), list):
                    is_match = rule.matches(context)
                elif rule.rule_type == RuleType.ACTION:
                    if 'condition' in rule.payload:
                        cond_payload = json.loads(rule.payload['condition'])
                        is_match = any(cond_payload.get(k, True) for k in ['context'] if isinstance(cond_payload[k], list))
                matched_rules.append(rule)
            except Exception as e:
                self.logger.error(f"Error evaluating rule {rule.rule_id}: {e}")
        return matched_rules
if __name__ == '__main__':
    config_file = 'decision_config.json'
    engine = DecisionEngine(config_path=config_file, log_level=logging.INFO)
    test_context = {"user_age": 25, "is_vip": True}
    results = engine.evaluate(test_context)
    print(f"Evaluated {len(results)} rules.")
    for rule in results:
        self.logger.info(f"Matched Rule ID: {rule.rule_id}")