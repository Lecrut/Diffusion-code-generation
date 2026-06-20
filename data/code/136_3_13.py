def filter_tuples(tuples, criteria):
    filtered = []
    for item in tuples:
        if all(item[i] > value for i, value in enumerate(criteria)):
            filtered.append(item)
    return filtered

if __name__ == '__main__':
    sample_tuples = [(10, 20), (30, 40), (50, 60)]
    criteria = (25, 35)
    result = filter_tuples(sample_tuples, criteria)
    print(f"Filtered Tuples: {result}")