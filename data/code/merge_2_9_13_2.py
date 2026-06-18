import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Callable, Optional
class RuleEngine:
    def __init__(self, config_path: str):
        self.rules: Dict[str, Dict[str, Any]] = {}
        self.logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
    def load_rules(self, config_path: str):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                raw_config = json.load(f)
            if not isinstance(raw_config, dict):
                raise ValueError("Configuration must be a dictionary.")
            self.rules = {}
            for rule_id, condition in raw_config.items():
                try:
                    if 'condition' not in condition or 'action' not in condition:
                        raise KeyError(f"Rule '{rule_id}' missing required keys 'condition' and/or 'action'.")
                    self.rules[rule_id] = {
                        "id": rule_id,
                        "condition": condition["condition"],
                        "action": condition["action"]
                    }
                except Exception as e:
                    self.logger.error(f"Failed to parse rule '{rule_id}': {str(e)}")
            if not self.rules:
                raise ValueError("No valid rules loaded.")
            self.logger.info(f"Successfully loaded {len(self.rules)} rules from {config_path}")
        except FileNotFoundError:
            self.logger.critical(f"Configuration file not found: {config_path}")
            raise
        except json.JSONDecodeError as e:
            self.logger.critical(f"Invalid JSON in configuration file: {str(e)}")
            raise
    def evaluate(self, data: Dict[str, Any]) -> Optional[Dict[str, str]]:
        for rule_id, rule_data in self.rules.items():
            condition = rule_data["condition"]
            try:
                if isinstance(condition, dict):
                    match = True
                    for field, expected_value in condition.items():
                        actual_value = data.get(field)
                        if actual_value != expected_value:
                            match = False
                            break
                elif isinstance(condition, list):
                    match = True
                    for item in condition:
                        if not item or item is None:
                            match = False
                            break
                else:
                    raise ValueError(f"Unsupported condition type for rule '{rule_id}': {type(condition)}")
                if match:
                    action_text = str(rule_data["action"])
                    self.logger.debug(f"Rule '{rule_id}' matched. Action: {action_text}")
                    return {"rule": rule_id, "status": "matched", "message": action_text}
            except Exception as e:
                self.logger.error(f"Evaluation error for rule '{rule_id}': {str(e)}")
        self.logger.debug("No rules matched.")
        return None
def generate_sample_config(config_path: str) -> Dict[str, Any]:
    config = {
        "user_active": {
            "condition": {"age": 18},
            "action": "Grant access"
        },
        "high_value_purchase": {
            "condition": ["amount > 500", "category == 'electronics'"],
            "action": "Flag for review"
        }
    }
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
if __name__ == '__main__':
    config_file = "rules_config.json"
    try:
        generate_sample_config(config_file)
        engine = RuleEngine(config_file)
        test_data_1 = {"age": 25, "amount": 300}
        result_1 = engine.evaluate(test_data_1)
        if not result_1:
            print("No match found for Test Data 1")
        else:
            print(f"Result: {result_1}")
    except Exception as e:
        logging.critical(f"Fatal error in execution: {str(e)}")