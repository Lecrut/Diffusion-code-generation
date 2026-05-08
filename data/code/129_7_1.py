from typing import List
class ComplexObject:
    def __init__(self, score: int, level: int):
        self.score = score
        self.level = level
def sort_complex_objects(data: List[ComplexObject]) -> List[ComplexObject]:
    return sorted(data, key=lambda obj: (-obj.level, obj.score))
if __name__ == '__main__':
    data = [
        ComplexObject(score=85, level=3),
        ComplexObject(score=92, level=1),
        ComplexObject(score=78, level=3),
        ComplexObject(score=95, level=1),
        ComplexObject(score=88, level=2)
    ]
    sorted_data = sort_complex_objects(data)
    for obj in sorted_data:
        print(f"Score: {obj.score}, Level: {obj.level}")