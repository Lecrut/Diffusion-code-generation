PRIMARY_KEY = 'category'
SECONDARY_KEY = 'name'

def sort_tuples(data):
    return sorted(data, key=lambda x: (-x[PRIMARY_KEY], x[SECONDARY_KEY]))

if __name__ == '__main__':
    sample_data = [
        ('A', 'Banana'),
        ('B', 'Apple'),
        ('A', 'Cherry'),
        ('B', 'Date'),
        ('A', 'Avocado'),
        ('C', 'Carrot')
    ]
    sorted_data = sort_tuples(sample_data)
    for item in sorted_data:
        print(item)