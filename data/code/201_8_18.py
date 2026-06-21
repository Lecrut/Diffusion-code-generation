class ScoreCalculator:
    @staticmethod
    def calculate_average(data):
        if not data:
            raise ValueError("Input data cannot be empty.")
        try:
            return sum(data) / len(data)
        except TypeError:
            raise TypeError("All elements in the input data must be numeric.")

if __name__ == '__main__':
    sample_data = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78
    }
    try:
        average_score = ScoreCalculator.calculate_average(sample_data.values())
        print(f"Average score: {average_score}")
    except (ValueError, TypeError) as e:
        print(e)