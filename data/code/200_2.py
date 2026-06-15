def filter_older_than_thirty(data):
    for person in data:
        if person['age'] > 30:
            print(person['name'])
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 32},
        {'name': 'Charlie', 'age': 40},
        {'name': 'David', 'age': 29},
        {'name': 'Eve', 'age': 30}
    ]
    filter_older_than_thirty(sample_data)