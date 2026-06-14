def sort_scores(data):
    sorted_data = sorted(data, key=lambda item: (-item[0], item[1]))
    return sorted_data
if __name__ == '__main__':
    sample_data = [
        (85, 'Alice'),
        (92, 'Bob'),
        (85, 'Charlie'),
        (92, 'Anna'),
        (78, 'David')
    ]
    result = sort_scores(sample_data)
    print(result)