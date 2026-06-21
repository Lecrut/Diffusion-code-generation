def compute_grades(scores):
    if not scores:
        return []
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    if n == 1:
        return [5]
    ranks = [0] * n
    for i, score in enumerate(sorted_scores):
        count_less = sum((1 for x in sorted_scores if x < score))
        count_equal = sum((1 for x in sorted_scores if x == score))
        avg_rank = count_less + count_equal / 2.0
        ranks[i] = avg_rank
    min_rank = min(ranks)
    max_rank = max(ranks)
    if max_rank == min_rank:
        if scores[0] == sorted_scores[-1]:
            return [5] * n
    normalized_ranks = [(r - min_rank) / (max_rank - min_rank) for r in ranks]
    score_to_grade = {}
    for i, norm_rank in enumerate(normalized_ranks):
        score_to_grade[sorted_scores[i]] = norm_rank

    def get_grade_from_norm_rank(norm_r):
        if norm_r > 0.9:
            return 5
        elif norm_r > 0.7:
            return 4
        elif norm_r > 0.4:
            return 3
        elif norm_r > 0.1:
            return 2
        else:
            return 1
    grades = []
    for score in scores:
        indices = [i for i, s in enumerate(sorted_scores) if s == score]
        if not indices:
            norm_r = 0.5
        else:
            avg_norm_r = sum((normalized_ranks[i] for i in indices)) / len(indices)
            norm_r = avg_norm_r
        grades.append(get_grade_from_norm_rank(norm_r))
    return grades
if __name__ == '__main__':
    scores = [95, 85, 75, 65, 55, 45, 35, 25, 15, 5]
    grades = compute_grades(scores)
    print(grades)