def calculate_average(score_list):
    if not score_list:
        return 0.0
    return sum(score_list) / len(score_list)

if __name__ == '__main__':
    scores = [85, 92, 78, 90, 88]
    print(calculate_average(scores))