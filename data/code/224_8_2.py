import sys
def calculate_mean(data):
    if not data:
        return 0.0
    return sum(data) / len(data)
if __name__ == '__main__':
    input_data = [10, 20.5, "30", "40"]
    scores = []
    all_valid = True
    for item in input_data:
        try:
            score = float(item)
            scores.append(score)
        except ValueError:
            all_valid = False
            break
    if not all_valid:
        sys.stderr.write("Error: One or more inputs were not valid numbers.\n")
    else:
        mean = calculate_mean(scores)
        print(f"{mean:.2f}")