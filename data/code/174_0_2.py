def student_scores():
    scores = {}
    def add_student(name, score):
        scores[name] = score
    def print_scores():
        for name, score in scores.items():
            print(f"{name}: {score}")
    add_student("Alice", 95)
    add_student("Bob", 88)
    add_student("Charlie", 92)
    print_scores()
if __name__ == '__main__':
    student_scores()