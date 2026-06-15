def sort_scores(data):
    return sorted(data, key=lambda item: (-item[0], item[1]))
if __name__ == '__main__':
    sample_data = [
        (85, "Charlie"),
        (92, "Alice"),
        (85, "Bob"),
        (92, "Zoe")
    ]
    sorted_data = sort_scores(sample_data)
    print(sorted_data)