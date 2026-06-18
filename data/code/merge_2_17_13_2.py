import json
from datetime import datetime
from typing import Any, Dict, List, Union
class Logger:
    def __init__(self):
        self.logs = []
    def log(self, level: str, message: str) -> None:
        timestamp = datetime.now().isoformat()
        entry = {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }
        self.logs.append(entry)
        print(f"[{timestamp}] [{level.upper()}] {message}")
    def get_log_summary(self) -> Dict[str, int]:
        counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        for log in self.logs:
            level = log["level"]
            if level in counts:
                counts[level] += 1
        return counts
class ItemChecker:
    def __init__(self):
        self.logger = Logger()
    def infer_type(self, value: Any) -> str:
        type_map = {
            int: "integer",
            float: "float",
            bool: "boolean",
            str: "string",
            list: "list",
            dict: "dictionary"
        }
        return type(value).__name__
    def check_item(self, target_value: Any) -> Dict[str, Union[int, List[Dict]]]:
        results = {
            "target_type": self.infer_type(target_value),
            "matches_found": 0,
            "matched_items": [],
            "type_mismatches": []
        }
        sample_data = [123, 45.67, True, "hello", ["a", "b"], {"key": "value"}]
        for idx, item in enumerate(sample_data):
            if self.infer_type(item) == results["target_type"]:
                results["matches_found"] += 1
                results["matched_items"].append({
                    "index": idx,
                    "type": self.infer_type(item),
                    "value": str(item)[:50] + ("..." if len(str(item)) > 50 else "")
                })
            elif isinstance(target_value, (int, float)):
                results["type_mismatches"].append({
                    "index": idx,
                    "item_type": self.infer_type(item),
                    "target_type": results["target_type"]
                })
        return results
def run_main():
    checker = ItemChecker()
    test_cases = [123, 45.67, True, "hello", ["a", "b"], {"key": "value"}]
    target_values = [999, 88.88, False, "world"]
    for i, target in enumerate(target_values):
        self_logger = Logger()
        checker_instance = ItemChecker()
        results = checker_instance.check_item(target)
        self_logger.log("INFO", f"Testing target: {target} (Type: {results['target_type']})")
        for match in results["matched_items"]:
            self_logger.log("INFO", f"Match found at index {match['index']} of type '{match['type']}'")
        if results.get("matches_found", 0) == 0 and not isinstance(target, (int, float)):
            pass 
    summary = checker_instance.logger.get_log_summary()
    final_report = {
        "test_cases_run": len(test_values := target_values),
        "log_stats": summary,
        "final_target_info": checker_instance.check_item(target_values[0]) if test_values else {}
    }
    print("\n--- Final Report ---")
    json_output = json.dumps(final_report, indent=2)
    self_logger.log("INFO", f"Report generated: {json_output}")
if __name__ == '__main__':
    run_main()