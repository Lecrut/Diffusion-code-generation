import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Callable
from dataclasses import dataclass, field
@dataclass
class Rule:
    condition: str = ""
    action: str = ""
    priority: int = 0
    def __post_init__(self):
        if not isinstance(self.condition, str) or self.condition.strip() == "":
            raise ValueError("Condition must be a non-empty string")
        if not isinstance(self.action, str) or self.action.strip() == "":
            raise ValueError("Action must be a non-empty string")
class RuleEngine:
    def __init__(self):
        self.rules: List[Rule] = []
        self.logger = logging.getLogger(__name__)
    def load_rules_from_file(self, file_path: str) -> int:
        try:
            with open(file_path, 'r') as f:
                config_data = json.load(f)
            if not isinstance(config_data, list):
                raise ValueError("Configuration must be a JSON array")
            loaded_count = 0
            for item in config_data:
                try:
                    rule = Rule(
                        condition=item.get('condition', ''),
                        action=item.get('action', ''),
                        priority=int(item.get('priority', 99)) if isinstance(item.get('priority'), str) else int(item['priority'])
                    )
                    self.rules.append(rule)
                    loaded_count += 1
                except (ValueError, TypeError):
                    self.logger.error(f"Failed to parse rule at index {config_data.index(item)}: {item}")
            return loaded_count
        except FileNotFoundError:
            raise ValueError(f"Configuration file not found: {file_path}")
    def sort_rules(self) -> None:
        if len(self.rules) > 1:
            self.rules.sort(key=lambda r: -r.priority)
            self.logger.info("Rules sorted by priority (descending)")
    def evaluate_condition(self, condition_str: str, data: Dict[str, Any]) -> bool:
        try:
            if "==" in condition_str or ">=" in condition_str or "<" in condition_str:
                parts = condition_str.split()
                value_to_check = float(data.get(parts[1], 0))
                op_map = {'>': '>', '<': '<', '>=': '>='}
                operator = op_map.get(parts[-2]) if len(parts) > 2 else '='
                target_value = parts[-1]
                return eval(f"{value_to_check} {operator} {target_value}")
            elif "in" in condition_str.lower():
                items = [x.strip() for x in condition_str.split(' or ')]
                if any(item in data.keys() and True for item in items):
                    return True
        except Exception as e:
            self.logger.error(f"Evaluation error for '{condition_str}': {e}")
        return False
    def execute(self, input_data: Dict[str, Any]) -> List[Dict[str, str]]:
        results = []
        if not self.rules:
            self.logger.warning("No rules loaded. Please load a configuration file first.")
            return results
        for rule in self.rules:
            if self.evaluate_condition(rule.condition, input_data):
                action_result = {
                    "rule": rule.action,
                    "priority": rule.priority,
                    "status": "executed"
                }
                if "log" in rule.action.lower():
                    self.logger.info(f"Executing: {rule.action}")
                results.append(action_result)
        return results
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    engine = RuleEngine()
    config_path = "rules_config.json"
    try:
        count = engine.load_rules_from_file(config_path)
        if count > 0:
            engine.sort_rules()
            input_data = {
                "temperature": 25.5,
                "humidity": 60,
                "status": "active"
            }
            results = engine.execute(input_data)
            print(f"\nExecution Results ({len(results)} rules triggered):")
            for r in results:
                print(f"- {r['rule']} (Priority: {r['priority']})")
        else:
            print("No valid rules found.")
    except ValueError as e:
        logging.error(str(e))