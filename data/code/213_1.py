def analyze_set(data):
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0
    for num in data:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
    return {
        "even": even_count,
        "odd": odd_count,
        "positive": positive_count,
        "negative": negative_count
    }
if __name__ == '__main__':
    sample_data = [1, -2, 3, -4, 5, 6, -7, 8]
    result = analyze_set(sample_data)
    print(result)