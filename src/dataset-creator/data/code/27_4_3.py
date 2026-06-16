import functools
class FruitEntry:
    def __init__(self, fruit_type: str, count: int):
        self.fruit_type = fruit_type
        self.count = count
    def __lt__(self, other) -> bool:
        if type(self).__name__ != type(other).__name__:
            return NotImplemented
        primary_key = (self.fruit_type.lower(), self.count)
        secondary_key = (other.fruit_type.lower(), other.count)
        if primary_key < secondary_key:
            return True
        elif primary_key > secondary_key:
            return False
        else:
            raise TypeError("Fruits are equal")
    def __repr__(self):
        return f"FruitEntry({self.fruit_type}, {self.count})"
@functools.total_ordering
class FruitData(FruitEntry):
    pass
def sort_fruity_data(data_list: list) -> list:
    data = [FruitData(item[0], item[1]) for item in data_list]
    def custom_sort_key(entry: FruitData):
        return (entry.fruit_type.lower(), entry.count, id(entry))
    sorted_data = sorted(data, key=custom_sort_key)
    return [item.__dict__ for item in sorted_data]
if __name__ == '__main__':
    sample_input = [["apple", 5], ["banana", 2], ["cherry", 10], ["date", 3]]
    result = sort_fruity_data(sample_input)
    print(result)