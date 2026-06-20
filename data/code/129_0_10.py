def filter_and_sort_people(people):
    return sorted(filter(lambda p: p['age'] > 25, people), key=lambda x: x['name'])

if __name__ == '__main__':
    sample_people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 24},
        {'name': 'Charlie', 'age': 35}
    ]
    filtered_sorted_people = filter_and_sort_people(sample_people)
    print(filtered_sorted_people)