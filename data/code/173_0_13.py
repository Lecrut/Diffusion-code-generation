from collections import defaultdict

def group_data(data_list, key):
    grouped_data = defaultdict(list)
    for item in data_list:
        if key in item:
            category = item[key]
            grouped_data[category].append(item)
    return dict(grouped_data)

if __name__ == '__main__':
    sample_data = [
        {'title': 'Python Programming', 'author': 'John Doe'},
        {'title': 'Advanced Python', 'author': 'Jane Smith'},
        {'title': 'Learning JavaScript', 'author': 'John Doe'}
    ]
    grouping_key = 'author'

    grouped_books = group_data(sample_data, grouping_key)
    print(grouped_books)