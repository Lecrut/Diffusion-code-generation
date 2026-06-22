def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_entries = [
        {'title': 'Book A', 'year': 2001},
        {'title': 'Book B', 'year': 1998},
        {'title': 'Book C', 'year': 2005}
    ]
    sorted_entries = sort_dicts_by_key(sample_entries, 'year')
    print(sorted_entries)