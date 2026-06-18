class DataObjectOrganizer:
    def sort_list(self, data_list, key):
        return sorted(data_list, key=lambda item: item[key])
if __name__ == '__main__':
    organizer = DataObjectOrganizer()
    sample_data = [
        {'name': 'Alice', 'age': 30, 'score': 85},
        {'name': 'Bob', 'age': 25, 'score': 92},
        {'name': 'Charlie', 'age': 35, 'score': 78}
    ]
    sort_by_age = organizer.sort_list(sample_data, 'age')
    print("Sorted by age:")
    for item in sort_by_age:
        print(item)
    sort_by_score = organizer.sort_list(sample_data, 'score')
    print("\nSorted by score:")
    for item in sort_by_score:
        print(item)