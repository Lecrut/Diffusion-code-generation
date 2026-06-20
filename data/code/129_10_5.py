def filter_and_sort(data, min_age, sort_key):
    filtered = [person for person in data if person['age'] >= min_age]
    sorted_data = sorted(filtered, key=lambda x: x[sort_key])
    return sorted_data

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    result = filter_and_sort(sample_data, min_age=21, sort_key='name')
    print(result)