grade_mapping = {0: "F", 1: "F", 2: "F", 3: "F", 4: "F", 5: "F", 6: "F", 7: "F", 8: "F", 9: "D", 10: "D", 11: "D", 12: "D", 13: "D", 14: "C", 15: "C", 16: "C", 17: "C", 18: "B", 19: "B", 20: "B", 21: "B", 22: "A", 23: "A", 24: "A", 25: "A", 26: "A", 27: "A", 28: "A", 29: "A", 30: "A"}

def convert_scores_to_grades(raw_scores):
    letter_grades = []
    for score in raw_scores:
        index = int(score // 10)
        if index > 30:
            index = 30
        letter_grades.append(grade_mapping[index])
    return letter_grades

if __name__ == '__main__':
    sample_scores = [45, 67, 82, 91, 55, 23, 30]
    result = convert_scores_to_grades(sample_scores)
    print(result)