from collections import defaultdict
from typing import List, NamedTuple

class Person(NamedTuple):
    name: str
    age: int
    city: str

def group_by_field(namedtuples: List[NamedTuple], field_name: str) -> dict:
    grouped = defaultdict(list)
    for nt in namedtuples:
        value = getattr(nt, field_name)
        grouped[value].append(nt)
    return dict(grouped)

if __name__ == '__main__':
    people = [
        Person('Alice', 30, 'New York'),
        Person('Bob', 25, 'Los Angeles'),
        Person('Charlie', 30, 'New York')
    ]
    grouped_people = group_by_field(people, 'city')
    print(grouped_people)