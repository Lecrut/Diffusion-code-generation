import sys
def calculate_averages(data):
    results = []
    for number_set in data:
        if not number_set:
            average = 0
        else:
            average = sum(number_set) / len(number_set)
        results.append(average)
    return results
if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [10, 20, 30, 40],
        [5, 5, 5, 5]
    ]
    averages = calculate_averages(sample_data)
    for avg in averages:
        print(avg)