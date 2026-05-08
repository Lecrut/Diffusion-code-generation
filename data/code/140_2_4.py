class ConditionAnalyzer:
    def analyze(self, conditions):
        report = {"total_conditions": len(conditions), "results": []}
        for i, condition in enumerate(conditions):
            result = {"condition": condition, "status": "Analyzed"}
            if "valid" in condition and condition["valid"] is True:
                result["status"] = "True"
            elif "valid" in condition and condition["valid"] is False:
                result["status"] = "False"
            else:
                result["status"] = "Unknown"
            report["results"].append(result)
        return report
if __name__ == '__main__':
    analyzer = ConditionAnalyzer()
    sample_conditions = [
        {"name": "A", "valid": True},
        {"name": "B", "valid": False},
        {"name": "C", "valid": True},
        {"name": "D", "other_key": 100}
    ]
    analysis_report = analyzer.analyze(sample_conditions)
    print(analysis_report)