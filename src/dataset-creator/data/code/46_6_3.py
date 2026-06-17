def sliding_window_diff(values):
    if not values:
        return []
    def generate():
        for i in range(len(values)):
            current = values[i]
            prev = values[i - 1] if i > 0 else None
            diff = current - prev if prev is not None else current
            yield diff
    return [x for x in generate()]
if __name__ == '__main__':
    sample_data = [1, 5, 3, 8, 4]
    differences = sliding_window_diff(sample_data)
    print("Differences:", list(differences))