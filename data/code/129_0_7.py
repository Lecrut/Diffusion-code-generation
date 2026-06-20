def filter_people(people):
    return [p for p in people if p['age'] > 25]

def sort_people_by_name(people):
    return sorted(people, key=lambda x: x['name'])

def filter_and_sort_people(people):
    filtered_people = filter_people(people)
    sorted_people = sort_people_by_name(filtered_people)
    return sorted_people

if __name__ == '__main__':
    sample_people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 24},
        {'name': 'Charlie', 'age': 35}
    ]
    result = filter_and_sort_people(sample_people)
    print(result)