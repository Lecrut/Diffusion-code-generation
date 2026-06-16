import asyncio
from typing import List, Dict, Any, Callable
from dataclasses import dataclass
@dataclass
class Rule:
    name: str
    condition: Callable[[Any], bool]
    action: Callable[[], Any]
def parse_rule_set(rules_data: List[Dict[str, Any]]) -> List[Rule]:
    return [
        Rule(
            name=r["name"],
            condition=eval(r["condition"]),
            action=lambda **kwargs: r["action"](**kwargs) if isinstance(r.get("action"), str) else lambda: eval(r["action"])()
        ) for r in rules_data
    ]
def execute_sequential(rules: List[Rule], state: Any = None) -> Dict[str, Any]:
    results = {}
    current_state = state
    for rule in rules:
        if not rule.condition(current_state):
            continue
        try:
            result = rule.action()
            results[f"{rule.name}_result"] = result
            current_state = {**current_state, "processed": True}
        except Exception as e:
            results[f"{rule.name}_error"] = str(e)
    return results
async def execute_concurrent(rules: List[Rule], state: Any = None) -> Dict[str, Any]:
    tasks = []
    for rule in rules:
        if not rule.condition(state):
            continue
        async def run_rule(r=rule):
            try:
                result = await asyncio.get_event_loop().run_in_executor(None, r.action)
                return f"{r.name}_result", result
            except Exception as e:
                return f"{r.name}_error", str(e)
        tasks.append(asyncio.create_task(run_rule(rule)))
    results = {}
    for task in asyncio.as_completed(tasks):
        name, value = await task
        if "error" not in name.lower():
            results[name] = value
        else:
            results[name] = {"status": "failed", "message": value}
    return results
if __name__ == '__main__':
    sample_rules_data = [
        {
            "name": "check_positive",
            "condition": "__import__('builtins').int(input('x')) > 0",
            "action": 'print("Value is positive")'
        },
        {
            "name": "calculate_square",
            "condition": '__import__("os").system("echo test") == True',
            "action": "__import__('builtins').int(input('x')) ** 2"
        }
    ]
    hardcoded_rules = [
        Rule(name="check_positive", condition=lambda x: x > 0, action=lambda: "Value is positive"),
        Rule(name="calculate_square", condition=lambda x: True, action=lambda: 25)
    ]
    sequential_output = execute_sequential(hardcoded_rules, state=10)
    concurrent_output = asyncio.run(execute_concurrent(hardcoded_rules, state=10))
    print("Sequential Results:", sequential_output)
    print("Concurrent Results:", concurrent_output)