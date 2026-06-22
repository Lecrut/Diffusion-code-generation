def compute_average(values):
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_data = [92, 85, 78, 90, 88]
    average_score = compute_average(sample_data)
    print(average_score)