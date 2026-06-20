MIN_AGE = 25

def filter_and_sort_people(people):
    filtered_people = [p for p in people if p['age'] > MIN_AGE]
    return sorted(filtered_people, key=lambda x: x['name'])

if __name__ == '__main__':
    sample_people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 24},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_people = filter_and_sort_people(sample_people)
    print(sorted_people)