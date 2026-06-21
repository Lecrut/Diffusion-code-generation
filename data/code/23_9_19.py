def get_grade(score):
    boundaries = [90, 80, 70, 60, 0]
    labels = ['A', 'B', 'C', 'D', 'F']
    current_grade = 'F'
    for boundary, label in zip(boundaries, labels):
        if score >= boundary:
            current_grade = label
            break
    return current_grade
if __name__ == '__main__':
    result = get_grade(88)
    print(result)
    result = get_grade(72)
    print(result)