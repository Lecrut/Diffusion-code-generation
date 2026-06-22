def get_grade(score: int) -> str:
    return 'F' if score < 60 else 'D' if score < 70 else 'C' if score < 80 else 'B' if score < 90 else 'A'

if __name__ == '__main__':
    print(get_grade(85))