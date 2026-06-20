def filter_and_sort_people(people):
    filtered_people = [p for p in people if p['age'] > 25]
    sorted_people = sorted(filtered_people, key=lambda x: x['name'])
    return sorted_people

if __name__ == '__main__':
    sample_people = [
        {'name': 'David', 'age': 28},
        {'name': 'Eve', 'age': 32},
        {'name': 'Frank', 'age': 24}
    ]
    result = filter_and_sort_people(sample_people)
    print(result)