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
    sample_input = [
        [1, 2, 3],
        [10, 20, 30, 40],
        [5],
        [],
        [1.5, 2.5]
    ]
    averages = calculate_averages(sample_input)
    for avg in averages:
        print(avg)