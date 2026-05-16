class ConditionAnalyzer:
    def analyze(self, conditions):
        report = {"total_conditions": len(conditions), "passed_count": 0, "failed_count": 0, "details": []}
        for condition in conditions:
            result = self._evaluate_condition(condition)
            report["details"].append({"condition": condition, "result": result})
            if result:
                report["passed_count"] += 1
            else:
                report["failed_count"] += 1
        return report
    def _evaluate_condition(self, condition):
        if isinstance(condition, str):
            return condition.lower() == "true"
        elif isinstance(condition, bool):
            return condition
        else:
            return False
if __name__ == '__main__':
    analyzer = ConditionAnalyzer()
    sample_conditions = [
        "True",
        "false",
        True,
        "TRUE",
        1,
        "No",
        False
    ]
    analysis_report = analyzer.analyze(sample_conditions)
    print(analysis_report)