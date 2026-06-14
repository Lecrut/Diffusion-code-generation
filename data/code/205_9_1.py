def sort_scores(data):
    return sorted(data, key=lambda item: (-item[0], item[1]))
if __name__ == '__main__':
    sample_data = [
        (85, 'Alice'),
        (92, 'Bob'),
        (85, 'Charlie'),
        (92, 'Anna'),
        (78, 'David')
    ]
    sorted_data = sort_scores(sample_data)
    print(sorted_data)