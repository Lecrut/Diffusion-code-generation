class DictSorter:
    def __init__(self, data):
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Input must be a list of dictionaries.")
        self.data = data

    def sort_by_key(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string.")
        return sorted(self.data, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'grade': 88},
        {'name': 'Bob', 'grade': 95},
        {'name': 'Charlie', 'grade': 79}
    ]
    sorter = DictSorter(sample_data)
    sorted_by_grade = sorter.sort_by_key('grade')
    print("Sorted by grade:", sorted_by_grade)

    sample_people = [
        {'name': 'David', 'age': 40},
        {'name': 'Eve', 'age': 32},
        {'name': 'Frank', 'age': 45}
    ]
    people_sorter = DictSorter(sample_people)
    sorted_by_age = people_sorter.sort_by_key('age')
    print("Sorted by age:", sorted_by_age)