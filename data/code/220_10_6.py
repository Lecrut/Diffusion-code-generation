import sys
def calculate_averages(data):
    results = []
    for s in data:
        if s:
            average = sum(s) / len(s)
            results.append(average)
        else:
            results.append(0)
    return results
if __name__ == '__main__':
    sample_input = [
        [1, 2, 3],
        [10, 20],
        [5, 5, 5, 5],
        [],
        [100]
    ]
    averages = calculate_averages(sample_input)
    for avg in averages:
        print(avg)