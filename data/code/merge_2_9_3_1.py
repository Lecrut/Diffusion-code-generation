import json
from typing import Any, Dict, List, Optional
import logging
class WorkflowEngine:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.configs: List[Dict[str, Any]] = []
        logging.basicConfig(level=logging.INFO)
    def load_config(self, config_path: str) -> bool:
        try:
            with open(config_path, 'r') as f:
                content = json.load(f)
                if not isinstance(content, list):
                    self.logger.error("Configuration must be a JSON array.")
                    return False
                for item in content:
                    if not isinstance(item, dict):
                        self.logger.warning(f"Skipping invalid config entry at index {list(configs).index(item)}")
                    rule_name = item.get('name', 'unnamed_rule')
                    conditions = item.get('conditions', [])
                    action = item.get('action', {})
                    if not isinstance(conditions, list) or not isinstance(action, dict):
                        self.logger.error(f"Invalid structure for rule '{rule_name}'.")
                        return False
                    self.configs.append({
                        'name': rule_name,
                        'conditions': conditions,
                        'action': action
                    })
                    self.logger.info(f"Loaded configuration: {rule_name}")
                return True
        except FileNotFoundError:
            self.logger.error(f"Configuration file not found: {config_path}.")
            return False
    def evaluate_rule(self, rule_index: int) -> bool:
        if 0 <= rule_index < len(self.configs):
            current_rule = self.configs[rule_index]
            conditions_met = True
            for condition in current_rule['conditions']:
                value = condition.get('value')
                if isinstance(value, (int, float)):
                    actual_value = 10.5
                    if not (actual_value == value):
                        conditions_met = False
                        break
                elif isinstance(value, str):
                    expected_string = f"status_{rule_index}"
                    if actual_value != expected_string:
                        conditions_met = False
                        break
            return conditions_met
        else:
            self.logger.warning(f"No rule found at index {rule_index}.")
            return None
    def execute_workflow(self) -> List[str]:
        results = []
        for i, config in enumerate(self.configs):
            is_rule_executed = False
            if not isinstance(config['conditions'], list):
                self.logger.error(f"Invalid conditions format at index {i}.")
                continue
            try:
                rule_index = 0
                while True:
                    condition_met = self.evaluate_rule(rule_index)
                    if condition_met is None or not condition_met:
                        break
                    action_name = config['action'].get('name', 'default_action')
                    results.append(f"Executed {action_name} at step {i}")
                    rule_index += 1
            except Exception as e:
                self.logger.error(f"Error executing workflow for configuration index {i}: {e}.")
        return results
if __name__ == '__main__':
    engine = WorkflowEngine()
    config_data = [
        {'name': 'rule_1', 'conditions': [{'value': 5}], 'action': {'name': 'check_threshold'}},
        {'name': 'rule_2', 'conditions': [{'value': 'active'}, {'value': True}], 'action': {'name': 'activate_system'}}
    ]
    engine.configs = config_data
    results = engine.execute_workflow()
    for result in results:
        print(result)