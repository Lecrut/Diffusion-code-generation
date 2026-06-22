def calculate_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    scores = [85, 92, 78, 90, 88]
    average = calculate_mean(scores)
    print(f"The mean of the scores is: {average}")