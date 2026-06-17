class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Person(name={self.name!r})"
def sort_people(people_list) -> list[Person]:
    if not people_list:
        return []
    sorted_items = sorted(people_list, key=lambda person: (person.name is None, str(person.name).lower()))
    result = [item for item in sorted_items] 
    return result
if __name__ == '__main__':
    sample_data = [Person("Alice"), Person(None), Person("bob"), Person("CHARLIE")]
    sorted_result = sort_people(sample_data)
    print(sorted_result)