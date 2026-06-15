import sys
if __name__ == '__main__':
    input_data = [10, 20.5, "30", "error", 40]
    scores = []
    for item in input_data:
        try:
            scores.append(float(item))
        except ValueError:
            pass
    if scores:
        mean_score = sum(scores) / len(scores)
        print(f"{mean_score:.2f}")
    else:
        print("No valid scores found")