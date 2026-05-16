class ConditionAnalyzer:
    def analyze(self, conditions):
        results = []
        for condition in conditions:
            analysis = {"condition": condition, "is_true": False, "notes": "No specific analysis"}
            if isinstance(condition, str):
                if "true" in condition.lower():
                    analysis["is_true"] = True
                    analysis["notes"] = "String condition evaluated as true"
                elif "false" in condition.lower():
                    analysis["is_true"] = False
                    analysis["notes"] = "String condition evaluated as false"
                else:
                    analysis["notes"] = "String condition evaluated as neither true nor false"
            elif isinstance(condition, bool):
                analysis["is_true"] = condition
                analysis["notes"] = "Boolean condition evaluated directly"
            else:
                analysis["notes"] = "Unsupported condition type"
            results.append(analysis)
        return {"analysis_report": results}
if __name__ == '__main__':
    analyzer = ConditionAnalyzer()
    sample_conditions = [
        "Is the light on true",
        "Temperature is 30",
        False,
        "System status is false",
        123
    ]
    report = analyzer.analyze(sample_conditions)
    print(report)