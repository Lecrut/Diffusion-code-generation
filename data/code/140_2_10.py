class ConditionAnalyzer:
    def analyze(self, conditions):
        report = {"total_conditions": len(conditions), "results": []}
        for i, condition in enumerate(conditions):
            result = {"condition": condition, "status": "analyzed"}
            if "positive" in condition.lower():
                result["status"] = "Positive"
            elif "negative" in condition.lower():
                result["status"] = "Negative"
            else:
                result["status"] = "Neutral"
            report["results"].append(result)
        return report
if __name__ == '__main__':
    analyzer = ConditionAnalyzer()
    sample_conditions = [
        "The temperature is positive",
        "The result is negative",
        "The value is zero",
        "Condition is positive and true",
        "Something is negative"
    ]
    analysis_report = analyzer.analyze(sample_conditions)
    print(analysis_report)