def filter_and_sort_people(people):
    filtered_people = [p for p in people if p['age'] > 25]
    sorted_people = sorted(filtered_people, key=lambda x: x['name'])
    return sorted_people

if __name__ == '__main__':
    sample_people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 24},
        {'name': 'Charlie', 'age': 35}
    ]
    result = filter_and_sort_people(sample_people)
    print(result)