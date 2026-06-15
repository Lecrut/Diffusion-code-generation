import sys
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    scores = input_data.split()
    total_sum = 0
    valid_count = 0
    for score in scores:
        try:
            total_sum += float(score)
            valid_count += 1
        except ValueError:
            pass
    if valid_count > 0:
        mean = total_sum / valid_count
        print(f"{mean:.2f}")
    else:
        print("No valid scores found")