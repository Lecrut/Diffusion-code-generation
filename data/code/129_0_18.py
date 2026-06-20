def filter_and_sort_people(people):
    return sorted([p for p in people if p['age'] > 25], key=lambda x: x['name'])

if __name__ == '__main__':
    sample_people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 24},
        {'name': 'Charlie', 'age': 26}
    ]
    print(filter_and_sort_people(sample_people))