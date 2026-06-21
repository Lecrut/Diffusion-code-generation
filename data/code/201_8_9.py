def calculate_average(data):
    if not data:
        return None
    try:
        total = sum(data.values())
        count = len(data)
        average = total / count
        return average
    except TypeError:
        raise TypeError("All values in the input dictionary must be numeric.")

if __name__ == '__main__':
    scores = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78,
        'David': 90
    }
    average_score = calculate_average(scores)
    print(f"Average Score: {average_score}")