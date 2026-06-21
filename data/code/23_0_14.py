def assign_grade(score: float) -> str:
    VALID_TYPES = (int, float)
    INVALID_TYPE_MSG = "score must be a number"
    VALID_RANGE_MIN = 0
    VALID_RANGE_MAX = 100
    INVALID_RANGE_MSG = "score must be between 0 and 100 inclusive"
    GRADE_A_THRESHOLD = 90
    GRADE_B_THRESHOLD = 80
    GRADE_C_THRESHOLD = 70
    GRADE_D_THRESHOLD = 60
    GRADE_F_THRESHOLD = 60
    if not isinstance(score, VALID_TYPES):
        raise TypeError(INVALID_TYPE_MSG)
    if score < VALID_RANGE_MIN or score > VALID_RANGE_MAX:
        raise ValueError(INVALID_RANGE_MSG)
    if score >= GRADE_A_THRESHOLD:
        return "A"
    if score >= GRADE_B_THRESHOLD:
        return "B"
    if score >= GRADE_C_THRESHOLD:
        return "C"
    if score >= GRADE_D_THRESHOLD:
        return "D"
    return "F"

if __name__ == '__main__':
    print(assign_grade(92.5))
    print(assign_grade(81))
    print(assign_grade(70.0))
    print(assign_grade(65))
    print(assign_grade(55))
    print(assign_grade(0))
    print(assign_grade(100))