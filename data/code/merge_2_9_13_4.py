import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Callable, Optional
class RuleEngine:
    def __init__(self, config_path: str):
        self.config = {}
        self.rules: Dict[str, List[Callable]] = {}
        self.logger = logging.getLogger(__name__)
        try:
            with open(config_path, 'r') as f:
                raw_config = json.load(f)
            if not isinstance(raw_config, dict):
                raise ValueError("Configuration must be a JSON object")
            for rule_name in raw_config.get('rules', {}):
                self.rules[rule_name] = []
                conditions = raw_config['rules'][rule_name].get('conditions', [])
                actions = raw_config['rules'][rule_name].get('actions', [])
                def make_condition(condition: Dict[str, Any], rule_name: str) -> Callable[[Dict[str, Any]], bool]:
                    return lambda data: self._evaluate_conditions(data, condition, rule_name)
                for cond in conditions:
                    self.rules[rule_name].append(make_condition(cond, rule_name))
        except FileNotFoundError as e:
            self.logger.error(f"Configuration file not found: {config_path}")
            raise
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON format in configuration: {e.msg}")
            raise
    def _evaluate_conditions(self, data: Dict[str, Any], condition: Dict[str, Any], rule_name: str) -> bool:
        if not isinstance(condition.get('field'), str):
            return False
        field = condition['field']
        operator = condition.get('operator', '==')
        value = condition.get('value')
        self.logger.debug(f"Evaluating condition for {rule_name}: Field '{field}' with op '{operator}' and val {value}")
        try:
            current_value = data[field] if field in data else None
            match operator == "==":
                case True: return current_value == value
                case "!=": return not (current_value == value)
                case "<": return current_value < value
                case ">": return current_value > value
                case "<=": return current_value <= value
                case ">=": return current_value >= value
            self.logger.warning(f"Unknown operator '{operator}' for rule {rule_name}")
            return False
        except KeyError as e:
            self.logger.error(f"Missing field in data for condition evaluation: {e.args[0]}")
            return False
    def evaluate(self, input_data: Dict[str, Any]) -> Optional[List[Any]]:
        results = []
        if not self.rules:
            self.logger.info("No rules loaded.")
            return None
        for rule_name in sorted(self.rules.keys()):
            conditions_met = all(rule(input_data) for rule in self.rules[rule_name])
            if conditions_met:
                actions = self._get_actions_for_rule(rule_name, input_data)
                results.extend(actions)
                self.logger.info(f"Rule '{rule_name}' triggered. Actions executed.")
        return results
    def _get_actions_for_rule(self, rule_name: str, data: Dict[str, Any]) -> List[Any]:
        actions = []
        for action in self.rules[rule_name].copy():
            if isinstance(action, dict) and 'action_type' in action:
                action_type = action['action_type']
                match action_type:
                    case "log":
                        message = f"Rule {rule_name} triggered. Data preview: {str(data)[:100]}"
                        self.logger.info(message)
                    case "modify_field":
                        field_to_modify = data.get(action.get('target', 'value')) if isinstance(field := action.get('field'), str) else None
                        try:
                            new_value = eval(str(action['new_value']))
                            for key, val in list(data.items()):
                                self.logger.debug(f"Modifying {key} from {val}")
                            data[field] = new_value if field_to_modify is not None and isinstance(field_to_modify, str) else (data.get(field), lambda: f"{field}: {new_value}" if field == 'value' else "N/A")
                        except Exception as e:
                            self.logger.error(f"Error executing action for rule {rule_name}: {e}")
                    case _:
                        self.logger.warning(f"Unknown action type '{action_type}' in rule {rule_name}. Skipping.")
        return results
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    config_path = "rules_config.json"
    try:
        engine = RuleEngine(config_path)
        sample_data = {"age": 25, "status": "active", "score": 80}
        output_actions = engine.evaluate(sample_data)
        if output_actions:
            print("Actions executed:")
            for action in output_actions:
                print(f"-> {action}")
    except Exception as e:
        logging.exception(e)