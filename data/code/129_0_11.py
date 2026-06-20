class PeopleFilterSorter:
    MIN_AGE = 25

    @staticmethod
    def filter_and_sort(people):
        return sorted([p for p in people if p['age'] > PeopleFilterSorter.MIN_AGE], key=lambda x: x['name'])

if __name__ == '__main__':
    sample_people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 24},
        {'name': 'Charlie', 'age': 35}
    ]
    result = PeopleFilterSorter.filter_and_sort(sample_people)
    print(result)