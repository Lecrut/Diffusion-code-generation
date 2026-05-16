class ConditionAnalyzer:
    def analyze(self, conditions):
        report = {"total_conditions": len(conditions), "positive_count": 0, "negative_count": 0, "neutral_count": 0, "details": []}
        for condition in conditions:
            result = self._evaluate_condition(condition)
            report["details"].append({"condition": condition, "result": result})
            if result == "True":
                report["positive_count"] += 1
            elif result == "False":
                report["negative_count"] += 1
            else:
                report["neutral_count"] += 1
        return report
    def _evaluate_condition(self, condition):
        if isinstance(condition, str):
            if condition.lower() == "true":
                return "True"
            elif condition.lower() == "false":
                return "False"
            elif condition.lower() == "yes":
                return "True"
            elif condition.lower() == "no":
                return "False"
            else:
                return "Neutral"
        elif isinstance(condition, bool):
            return "True" if condition else "False"
        else:
            return "Error: Invalid Type"
if __name__ == '__main__':
    analyzer = ConditionAnalyzer()
    sample_conditions = [
        "True",
        "False",
        "Yes",
        "No",
        "Maybe",
        True,
        False,
        123
    ]
    analysis_report = analyzer.analyze(sample_conditions)
    print(analysis_report)