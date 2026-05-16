class ConditionAnalyzer:
    def analyze(self, conditions):
        report = {"total_conditions": len(conditions), "positive_count": 0, "negative_count": 0, "neutral_count": 0, "details": []}
        for condition in conditions:
            if condition == "True":
                report["positive_count"] += 1
            elif condition == "False":
                report["negative_count"] += 1
            else:
                report["neutral_count"] += 1
            report["details"].append({"condition": condition, "status": "Positive" if condition == "True" else ("Negative" if condition == "False" else "Neutral")})
        return report
if __name__ == '__main__':
    analyzer = ConditionAnalyzer()
    sample_conditions = ["True", "False", "True", "True", "False", "Unknown"]
    analysis_report = analyzer.analyze(sample_conditions)
    print(analysis_report)