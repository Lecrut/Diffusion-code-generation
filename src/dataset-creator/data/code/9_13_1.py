import json
import logging
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Any, List, Callable
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
@dataclass(frozen=True)
class Rule:
    name: str
    condition: Callable[[Any], bool]
    action: Callable[[], Any]
def load_rules_from_config(config_path: Path) -> List[Rule]:
    if not config_path.exists():
        logger.error(f"Configuration file not found: {config_path}")
        return []
    try:
        with open(config_path, 'r') as f:
            data = json.load(f)
        rules = []
        for item in data.get('rules', []):
            if isinstance(item, dict) and 'name' in item and 'condition' in item and 'action' in item:
                cond_str = str(item['condition'])
                act_str = str(item['action'])
                try:
                    condition_func = eval(cond_str)
                    action_func = eval(act_str)
                    rule = Rule(
                        name=item.get('name', f"rule_{len(rules)+1}"),
                        condition=condition_func,
                        action=action_func
                    )
                    rules.append(rule)
                except Exception as e:
                    logger.error(f"Failed to parse rule '{item.get('name')}': {e}")
        return rules
    except json.JSONDecodeError as je:
        logger.error(f"Invalid JSON in configuration file: {je}")
        raise
def evaluate_rules(data: Any, rules: List[Rule]) -> Dict[str, Any]:
    results = {}
    for rule in rules:
        try:
            if rule.condition(data):
                result_data = rule.action()
                logger.debug(f"Rule '{rule.name}' triggered. Result: {result_data}")
                results[f"{rule.name}_action"] = result_data
            else:
                logger.info(f"Rule '{rule.name}' condition not met.")
        except Exception as e:
            logger.error(f"Error executing rule '{rule.name}': {e}")
    return results
if __name__ == '__main__':
    config_path = Path('config.json')
    try:
        rules = load_rules_from_config(config_path)
        sample_data = {"user_age": 25, "is_admin": False}
        final_results = evaluate_rules(sample_data, rules)
        logger.info(f"Final Decision Results: {final_results}")
    except Exception as e:
        logger.critical(f"FATAL ERROR in decision framework initialization: {e}", exc_info=True)