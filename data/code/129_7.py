class ComplexObject:
    def __init__(self, score, level):
        self.score = score
        self.level = level
def sort_complex_objects(data):
    return sorted(data, key=lambda x: (-x.level, x.score))
if __name__ == '__main__':
    objects = [
        ComplexObject(score=85, level=3),
        ComplexObject(score=92, level=1),
        ComplexObject(score=78, level=3),
        ComplexObject(score=95, level=1),
        ComplexObject(score=88, level=2)
    ]
    sorted_objects = sort_complex_objects(objects)
    for obj in sorted_objects:
        print(f"Score: {obj.score}, Level: {obj.level}")