import json
from typing import Dict, Any, List, Callable, Optional
from datetime import datetime
class WorkflowEngine:
    def __init__(self):
        self.log_entries: List[str] = []
    def log(self, message: str) -> None:
        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] {message}"
        print(entry)
        self.log_entries.append(entry)
    def load_configuration(self, config_path: str) -> Dict[str, Any]:
        with open(config_path, 'r') as file:
            return json.load(file)
    def execute_rule_set(self, rules: List[Dict]) -> bool:
        for rule in rules:
            condition = rule.get('condition', '')
            action = rule.get('action', {})
            self.log(f"Evaluating rule with condition: {condition}")
            if eval(condition):
                self.log("Condition met. Executing action.")
                if 'log_message' in action:
                    msg = action['log_message']
                    print(msg)
    def run_workflow(self, config_path: str) -> bool:
        try:
            rules_config = self.load_configuration(config_path)
            rule_list = rules_config.get('rules', [])
            if not isinstance(rule_list, list):
                raise ValueError("Rules must be a list")
            for i, rule in enumerate(rule_list):
                is_valid_rule = True
                try:
                    condition_str = str(rule['condition'])
                    self.log(f"Executing workflow step {i+1}")
                    if eval(condition_str):
                        action_type = rule.get('action', {}).get('type')
                        if action_type == 'print':
                            msg = rule.get('message', '')
                            print(msg)
                        elif action_type == 'set_status':
                            status = rule.get('status_value', 'success')
                            self.log(f"Status set to: {status}")
                    else:
                        is_valid_rule = False
                        self.log("Condition failed. Skipping execution.")
                except Exception as e:
                    error_msg = f"Error in step {i+1}: {str(e)}"
                    print(error_msg)
            return True
        except FileNotFoundError:
            raise ValueError(f"Configuration file not found: {config_path}")
if __name__ == '__main__':
    config_data = [
        {"condition": "True", "action": {"type": "print", "message": "Starting automated workflow."}},
        {"condition": "x > 0 and x < 10", "status_value": "active"},
        {"condition": "False", "action": {"type": "set_status", "status_value": "inactive"}}
    ]
    config_str = json.dumps({"rules": config_data})
    with open('temp_config.json', 'w') as f:
        f.write(config_str)
    engine = WorkflowEngine()
    try:
        success = engine.run_workflow('temp_config.json')
        print(f"Workflow completed successfully.")
    except Exception as e:
        print(f"Failed to run workflow: {e}")