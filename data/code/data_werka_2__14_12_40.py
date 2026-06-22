class VolumeAnalyzer:
    def __init__(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers.")
        self.volume1 = volume1
        self.volume2 = volume2

    def analyze(self):
        if self.volume1 > self.volume2:
            return "First volume is greater than the second."
        elif self.volume1 < self.volume2:
            return "First volume is less than the second."
        else:
            return "Both volumes are equal."

    def detailed_report(self):
        report = []
        if self.volume1 > self.volume2:
            report.append("First volume is greater than the second.")
        elif self.volume1 < self.volume2:
            report.append("First volume is less than the second.")
        else:
            report.append("Both volumes are equal.")

        difference = abs(self.volume1 - self.volume2)
        report.append(f"Difference between volumes: {difference}")

        return "\n".join(report)

if __name__ == '__main__':
    try:
        analyzer = VolumeAnalyzer(6.7890, 3.14159)
        print(analyzer.analyze())
        print(analyzer.detailed_report())
    except ValueError as e:
        print(e)