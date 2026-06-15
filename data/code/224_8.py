import sys
def calculate_mean(input_data):
    scores = []
    for line in input_data.strip().split('\n'):
        try:
            score = float(line.strip())
            scores.append(score)
        except ValueError:
            pass
    if not scores:
        return None
    mean = sum(scores) / len(scores)
    return mean
if __name__ == '__main__':
    sample_input = "10\n20.5\n30\n40"
    result = calculate_mean(sample_input)
    if result is not None:
        print(f"{result:.2f}")