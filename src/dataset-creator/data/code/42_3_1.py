def sort_mixed_data(data):
    converted = []
    for item in data:
        if isinstance(item, (int, float)):
            converted.append(str(float(item)))
        else:
            converted.append(str(item))
    return ",".join(sorted(converted))
if __name__ == '__main__':
    sample_data = [42, "banana", 3.14, "apple", 789]
    result = sort_mixed_data(sample_data)
    print(result)