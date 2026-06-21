class ScoreCalculator:
    @staticmethod
    def calculate_average(data):
        if not data:
            raise ValueError("Input data cannot be empty.")
        return sum(data) / len(data)

if __name__ == '__main__':
    sample_scores = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78
    }
    
    try:
        average_score = ScoreCalculator.calculate_average(sample_scores.values())
        print(f"Average score: {average_score}")
    except ValueError as e:
        print(e)