import random
def get_sort_key(record):
    age = record['age']
    status = record['status'].lower()
    if age >= 60 and status == 'senior':
        return (1, -age)
    elif age < 30 or status in ['student', 'junior']:
        return (2, age)
    else:
        return (0, -age)
def sort_records(records):
    sorted_data = sorted(records, key=get_sort_key)
    for item in sorted_data:
        print(f"{item['name']}: {item['email']}")
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25, 'status': 'student', 'email': 'alice@example.com'},
        {'name': 'Bob', 'age': 35, 'status': 'active', 'email': 'bob@example.com'},
        {'name': 'Charlie', 'age': 65, 'status': 'senior', 'email': 'charlie@example.com'},
        {'name': 'Diana', 'age': 28, 'status': 'junior', 'email': 'diana@example.com'}
    ]
    sort_records(sample_data)