def determine_status(score):
    return "Excellent" if score >= 90 else ("Good" if score >= 80 else ("Average" if score >= 70 else ("Below Average" if score >= 60 else "Fail")))

if __name__ == '__main__':
    print(determine_status(85))