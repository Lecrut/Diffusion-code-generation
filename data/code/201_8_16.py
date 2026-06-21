def calculate_average(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    scores1 = [85, 92, 78, 90]
    scores2 = [4.5, 3.8, 5.2, 4.9]
    scores3 = [-5, -3, -2, -4]

    print(f"Average of {scores1}: {calculate_average(scores1)}")
    print(f"Average of {scores2}: {calculate_average(scores2)}")
    print(f"Average of {scores3}: {calculate_average(scores3)}")