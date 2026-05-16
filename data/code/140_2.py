class ConditionAnalyzer:
    def analyze(self, conditions):
        results = []
        for condition in conditions:
            analysis = {"condition": condition, "is_true": False, "reason": "Not evaluated"}
            if isinstance(condition, str):
                if "true" in condition.lower():
                    analysis["is_true"] = True
                    analysis["reason"] = "String contains 'true'"
                elif "false" in condition.lower():
                    analysis["is_true"] = False
                    analysis["reason"] = "String contains 'false'"
                else:
                    analysis["reason"] = "String does not contain 'true' or 'false'"
            elif isinstance(condition, bool):
                analysis["is_true"] = condition
                analysis["reason"] = "Boolean value provided"
            else:
                analysis["reason"] = "Unsupported condition type"
            results.append(analysis)
        return {"analysis_report": results}
if __name__ == '__main__':
    analyzer = ConditionAnalyzer()
    sample_conditions = [
        "Condition A is true",
        "Condition B is false",
        True,
        "Condition C is neither true nor false",
        123
    ]
    report = analyzer.analyze(sample_conditions)
    print(report)