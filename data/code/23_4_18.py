class GradingPolicy:
    def __init__(self):
        self._boundaries = [
            (90, "A"),
            (80, "B"),
            (70, "C"),
            (60, "D"),
            (0, "F")
        ]

    def add_boundary(self, min_score, grade):
        self._boundaries.append((min_score, grade))
        self._boundaries.sort(key=lambda x: x[0], reverse=True)

    def evaluate(self, score):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a numeric type")
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        for threshold, grade in self._boundaries:
            if score >= threshold:
                return grade
        return "F"

if __name__ == "__main__":
    policy = GradingPolicy()
    result_a = policy.evaluate(95)
    result_b = policy.evaluate(85)
    result_c = policy.evaluate(75)
    result_d = policy.evaluate(65)
    result_f = policy.evaluate(50)
    print(result_a)
    print(result_b)
    print(result_c)
    print(result_d)
    print(result_f)