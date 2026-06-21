import typing

def fetch_column_values(data: typing.List[typing.Dict[str, typing.Any]], column_name: str) -> typing.List[typing.Any]:
    results = []
    for record in data:
        if column_name in record:
            results.append(record[column_name])
    return results

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 30},
        {'id': 2, 'name': 'Bob', 'age': 25},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    
    target_column = 'name'
    values = fetch_column_values(sample_data, target_column)
    print(values)