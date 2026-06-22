def convert_scores(raw_scores, grade_map):
    return [grade_map[score] for score in raw_scores]

if __name__ == '__main__':
    raw_scores = [95, 82, 76, 69, 58]
    grade_map = {
        90: 'A',
        80: 'B',
        70: 'C',
        60: 'D',
        0: 'F'
    }
    result = convert_scores(raw_scores, grade_map)
    print(result)