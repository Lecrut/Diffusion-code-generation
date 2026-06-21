def convert_scores(raw_scores):
    grade_map = {
        9: 'A',
        8: 'B',
        7: 'C',
        6: 'D',
        5: 'F',
        4: 'F',
        3: 'F',
        2: 'F',
        1: 'F',
        0: 'F'
    }
    return [grade_map[score // 10] for score in raw_scores]

if __name__ == '__main__':
    scores = [95, 82, 76, 65, 55, 100, 59]
    print(convert_scores(scores))