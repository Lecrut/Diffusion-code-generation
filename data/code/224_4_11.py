class ScoreProcessor:
    @staticmethod
    def calculate_mean(scores):
        if not scores:
            raise ValueError("Input sequence is empty")
        return sum(scores) / len(scores)

if __name__ == '__main__':
    processor = ScoreProcessor()
    sample_scores = (85, 90, 78, 92)
    result = processor.calculate_mean(sample_scores)
    print(result)