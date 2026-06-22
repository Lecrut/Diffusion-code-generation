def convert_scores(raw_scores):
    score_map = {
        range(90, 101): 'A',
        range(80, 90): 'B',
        range(70, 80): 'C',
        range(60, 70): 'D',
        range(-1, 60): 'F'
    }
    result = []
    for score in raw_scores:
        for grade_range, letter in score_map.items():
            if score in grade_range:
                result.append(letter)
                break
    return result

if __name__ == '__main__':
    raw_scores = [95, 82, 76, 65, 55, 100, 59]
    grades = convert_scores(raw_scores)
    print(grades)