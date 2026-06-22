def generate_grades(scores):
    for score in scores:
        try:
            numeric_score = float(score)
            if 0 <= numeric_score <= 100:
                if numeric_score >= 90:
                    yield 'A'
                elif numeric_score >= 80:
                    yield 'B'
                elif numeric_score >= 70:
                    yield 'C'
                elif numeric_score >= 60:
                    yield 'D'
                else:
                    yield 'F'
        except (ValueError, TypeError):
            continue

if __name__ == '__main__':
    sample_scores = [85.5, 92, 'invalid', 45, '70', 'abc', 101, 30.2]
    for grade in generate_grades(sample_scores):
        print(grade)