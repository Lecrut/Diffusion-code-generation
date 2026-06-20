def filter_and_sort_people(people):
    if not all(isinstance(p, dict) and 'age' in p and 'name' in p for p in people):
        raise ValueError("Invalid input: All items must be dictionaries with 'age' and 'name' keys.")
    
    filtered = [p for p in people if p['age'] > 25]
    sorted_people = sorted(filtered, key=lambda x: x['name'])
    return sorted_people

if __name__ == '__main__':
    sample_people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 24},
        {'name': 'Charlie', 'age': 35}
    ]
    try:
        result = filter_and_sort_people(sample_people)
        print(result)
    except ValueError as e:
        print(e)