def filter_and_sort_people(people):
    filtered = [p for p in people if p['age'] > 25]
    return sorted(filtered, key=lambda x: x['name'])

if __name__ == '__main__':
    sample_people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 24},
        {'name': 'Charlie', 'age': 35}
    ]
    result = filter_and_sort_people(sample_people)
    print(result)