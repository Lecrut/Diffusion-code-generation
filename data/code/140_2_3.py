class ConditionAnalyzer:
    def analyze(self, conditions):
        results = []
        for condition in conditions:
            analysis = {"condition": condition, "is_true": False, "details": []}
            if isinstance(condition, str):
                analysis["is_true"] = condition.lower() == "true"
                analysis["details"].append("String comparison performed.")
            elif isinstance(condition, bool):
                analysis["is_true"] = condition
                analysis["details"].append("Boolean value evaluated.")
            elif isinstance(condition, int) or isinstance(condition, float):
                analysis["is_true"] = condition > 0
                analysis["details"].append("Numeric value checked against zero.")
            else:
                analysis["is_true"] = None
                analysis["details"].append("Unsupported condition type.")
            results.append(analysis)
        return {"analysis_report": results}
if __name__ == '__main__':
    analyzer = ConditionAnalyzer()
    sample_conditions = [
        "True",
        "False",
        True,
        10,
        -5,
        "True",
        3.14,
        None
    ]
    report = analyzer.analyze(sample_conditions)
    print(report)